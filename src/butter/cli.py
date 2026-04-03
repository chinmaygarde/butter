import os
import subprocess
from pathlib import Path

import click
from rich.console import Console

from butter.doctor import doctor

console = Console()
err_console = Console(stderr=True)


@click.group()
@click.version_option(package_name="butter")
def cli() -> None:
    """butter: BTRFS-backed isolated development environments."""


cli.add_command(doctor)


@cli.command()
@click.argument("path", type=click.Path())
def init(path: str) -> None:
    """Initialize a butter repo at PATH."""
    result = subprocess.run(
        ["btrfs", "subvolume", "create", path],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        os.setxattr(path, b"user.butter.repo", os.path.basename(path).encode())
        console.print(f"[green]initialized[/green] repo at {path!r}")
    else:
        err_console.print(f"[red]error:[/red] {result.stderr.strip()}")
        raise SystemExit(result.returncode)


def _find_repo(start: Path) -> tuple[Path, str] | None:
    for directory in [start, *start.parents]:
        try:
            name = os.getxattr(directory, b"user.butter.repo").decode()
            return directory, name
        except OSError:
            continue
    return None


@cli.command()
def info() -> None:
    """Show information about the current butter repo."""
    result = _find_repo(Path.cwd())
    if result is None:
        err_console.print("[red]error:[/red] not inside a butter repo")
        raise SystemExit(1)
    path, name = result
    console.print(f"[bold]repo:[/bold] {name}")
    console.print(f"[bold]path:[/bold] {path}")


def main() -> None:
    cli()
