# butter

> BTRFS-backed isolated development environments

> [!CAUTION]
> This tool is still under development and not ready for use yet.

[![CI](https://github.com/chinmaygarde/butter/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/chinmaygarde/butter/actions/workflows/ci.yml)

## Goals

`butter` brings Git-worktree-style workflow to the filesystem level using [BTRFS](https://btrfs.readthedocs.io/) subvolumes and copy-on-write (CoW) snapshots.

- **Filesystem-level isolation** — each worktree is a BTRFS subvolume, not a symlink or copy. Processes, build artifacts, and tooling state are fully separated.
- **Space efficiency** — subvolumes are created via CoW snapshots. Only changed blocks are stored on disk; a fresh worktree costs nearly nothing.
- **Fast environment switching** — no containers, no VMs. Switching environments is as fast as changing a directory.

## Requirements

### End users

- Linux with a BTRFS-formatted filesystem
- Python 3.12+
- `btrfs-progs` (`btrfs` binary in PATH)
- Root / sudo access for BTRFS subvolume operations

### Development

All of the above, plus:

- [`uv`](https://docs.astral.sh/uv/) (package manager)
- [`just`](https://github.com/casey/just) (task runner)

## Installation

```bash
uv tool install butter-tree
```

Or from source:

```bash
git clone https://github.com/chinmaygarde/butter.git
cd butter
just install
```

## Quick Start

Before using butter, verify your system meets all requirements. Run from the directory where you plan to work — the filesystem check tests whether that directory resides on BTRFS:

```bash
butter doctor filesystem
```

Initialize a butter repo at a path on a BTRFS filesystem:

```bash
butter init /mnt/btrfs/myproject
```

Once inside a repo, inspect it with `info`:

```bash
cd /mnt/btrfs/myproject
butter info
```

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
