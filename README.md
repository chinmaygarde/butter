# butter

> BTRFS-backed isolated development environments

> [!CAUTION]
> This tool is still under development and not ready for use yet.

[![CI](https://github.com/chinmaygarde/butter/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/chinmaygarde/butter/actions/workflows/ci.yml)

## Goals

`butter` brings Git-worktree-style workflow to the filesystem level using [BTRFS](https://btrfs.readthedocs.io/) subvolumes and copy-on-write (CoW) snapshots.

- **Filesystem-level isolation** — each worktree is a BTRFS subvolume, not a symlink or copy. Processes, build artifacts, and tooling state are fully separated.
- **Space efficiency** — subvolumes are created via CoW snapshots. Only changed blocks are stored on disk; a fresh worktree costs nearly nothing.
- **Familiar CLI** — commands mirror `git worktree`: `add`, `list`, `remove`. If you know Git worktrees, you already know `butter`.
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

Before using butter, verify your system meets all requirements:

```bash
# Check OS, filesystem, and btrfs binary
butter doctor filesystem
```

Initialize a butter repo at the given path (creates a BTRFS subvolume and marks it with a `user.butter.repo` xattr):

```bash
butter init /mnt/btrfs/myproject
```

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
