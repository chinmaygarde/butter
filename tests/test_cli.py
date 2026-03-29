from click.testing import CliRunner

from butter_tree.cli import cli


def test_help():
    result = CliRunner().invoke(cli, ["--help"])
    assert result.exit_code == 0


def test_add_help():
    result = CliRunner().invoke(cli, ["add", "--help"])
    assert result.exit_code == 0


def test_list_help():
    result = CliRunner().invoke(cli, ["list", "--help"])
    assert result.exit_code == 0


def test_remove_help():
    result = CliRunner().invoke(cli, ["remove", "--help"])
    assert result.exit_code == 0
