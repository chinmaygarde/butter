import os

from click.testing import CliRunner

from butter.cli import cli


def test_help():
    result = CliRunner().invoke(cli, ["--help"])
    assert result.exit_code == 0


def test_info_help():
    result = CliRunner().invoke(cli, ["info", "--help"])
    assert result.exit_code == 0


def test_info_inside_repo(tmp_path):
    os.setxattr(tmp_path, b"user.butter.repo", b"myrepo")
    orig = os.getcwd()
    try:
        os.chdir(tmp_path)
        result = CliRunner().invoke(cli, ["info"], catch_exceptions=False)
    finally:
        os.chdir(orig)
    assert result.exit_code == 0
    assert "myrepo" in result.output


def test_info_outside_repo(tmp_path):
    orig = os.getcwd()
    try:
        os.chdir(tmp_path)
        result = CliRunner().invoke(cli, ["info"], catch_exceptions=False)
    finally:
        os.chdir(orig)
    assert result.exit_code == 1
