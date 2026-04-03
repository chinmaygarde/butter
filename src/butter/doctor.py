import ctypes
import platform
import shutil
import sys
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

console = Console()

_BTRFS_MAGIC = 0x9123683E


class _Statfs(ctypes.Structure):
    _fields_ = [
        ("f_type", ctypes.c_long),
        ("f_bsize", ctypes.c_long),
        ("f_blocks", ctypes.c_ulong),
        ("f_bfree", ctypes.c_ulong),
        ("f_bavail", ctypes.c_ulong),
        ("f_files", ctypes.c_ulong),
        ("f_ffree", ctypes.c_ulong),
        ("f_fsid", ctypes.c_long * 2),
        ("f_namelen", ctypes.c_long),
        ("f_frsize", ctypes.c_long),
        ("f_flags", ctypes.c_long),
        ("f_spare", ctypes.c_long * 4),
    ]


def _is_btrfs(path: Path) -> bool:
    buf = _Statfs()
    if (
        ctypes.CDLL(None, use_errno=True).statfs(str(path).encode(), ctypes.byref(buf))
        != 0
    ):
        return False
    return buf.f_type == _BTRFS_MAGIC


@click.group()
def doctor() -> None:
    """Check system compatibility with butter."""


@doctor.command()
def filesystem() -> None:
    """Check that the current directory resides on a BTRFS filesystem."""
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("check", style="bold")
    table.add_column("status")
    table.add_column("detail", style="dim")

    all_ok = True

    # Linux check
    is_linux = platform.system() == "Linux"
    if is_linux:
        table.add_row("operating system", "[green]ok[/green]", platform.system())
    else:
        table.add_row(
            "operating system",
            "[red]fail[/red]",
            f"{platform.system()} — butter requires Linux",
        )
        all_ok = False

    # BTRFS check
    if is_linux:
        cwd = Path.cwd()
        if _is_btrfs(cwd):
            table.add_row("filesystem", "[green]ok[/green]", f"{cwd} is BTRFS")
        else:
            table.add_row(
                "filesystem",
                "[red]fail[/red]",
                f"{cwd} is not BTRFS",
            )
            all_ok = False
    else:
        table.add_row("filesystem", "[yellow]skip[/yellow]", "skipped on non-Linux")

    # btrfs binary check
    btrfs_bin = shutil.which("btrfs")
    if btrfs_bin:
        table.add_row("btrfs binary", "[green]ok[/green]", btrfs_bin)
    else:
        table.add_row("btrfs binary", "[red]fail[/red]", "btrfs not found in PATH")
        all_ok = False

    console.print(table)
    sys.exit(0 if all_ok else 1)
