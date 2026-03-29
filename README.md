# butter

> BTRFS-backed isolated development environments

![CI](https://github.com/your-org/butter/actions/workflows/ci.yml/badge.svg)

## Goals

`butter` brings Git-worktree-style workflow to the filesystem level using [BTRFS](https://btrfs.readthedocs.io/) subvolumes and copy-on-write (CoW) snapshots.

- **Filesystem-level isolation** — each worktree is a BTRFS subvolume, not a symlink or copy. Processes, build artifacts, and tooling state are fully separated.
- **Space efficiency** — subvolumes are created via CoW snapshots. Only changed blocks are stored on disk; a fresh worktree costs nearly nothing.
- **Familiar CLI** — commands mirror `git worktree`: `add`, `list`, `remove`. If you know Git worktrees, you already know `butter`.
- **Fast environment switching** — no containers, no VMs. Switching environments is as fast as changing a directory.

## Requirements

- Linux with a BTRFS-formatted filesystem
- Python 3.12+
- `just` (task runner)
- Root / sudo access for BTRFS subvolume operations

## Installation

```bash
uv tool install butter
```

Or from source:

```bash
git clone https://github.com/your-org/butter.git
cd butter
just install
```

## Quick Start

```bash
# Create a new isolated environment named "feature-x" from the current directory
butter add feature-x

# Create from an explicit source path
butter add experiment /mnt/btrfs/projects/myproject

# List all managed worktrees
butter list

# Remove a worktree and its subvolume
butter remove feature-x
```

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
