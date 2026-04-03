import subprocess

import click
from rich.console import Console

from butter_tree.doctor import doctor

console = Console()


@click.group()
@click.version_option()
def cli() -> None:
    """butter: BTRFS-backed isolated development environments."""


cli.add_command(doctor)


@cli.command()
@click.argument("name")
@click.argument("source", default=".")
def add(name: str, source: str) -> None:
    """Create a new worktree named NAME from SOURCE path."""
    console.print(f"[bold]add[/bold] {name!r} from {source!r} — not yet implemented")


@cli.command(name="list")
def list_worktrees() -> None:
    """List all managed worktrees."""
    console.print("[bold]list[/bold] — not yet implemented")


@cli.command()
@click.argument("name")
def remove(name: str) -> None:
    """Remove the worktree named NAME."""
    console.print(f"[bold]remove[/bold] {name!r} — not yet implemented")


@cli.command()
@click.argument("path", type=click.Path())
def init(path: str) -> None:
    """Create a BTRFS subvolume at PATH."""
    result = subprocess.run(
        ["btrfs", "subvolume", "create", path],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        console.print(f"[green]created[/green] subvolume at {path!r}")
    else:
        console.print(f"[red]error:[/red] {result.stderr.strip()}", err=True)
        raise SystemExit(result.returncode)


def main() -> None:
    cli()
