from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable
import subprocess

import pytest

from littlegit import Git


@pytest.fixture()
def repo():
    with TemporaryDirectory() as temp_dir:
        repo_path = Path(temp_dir)

        subprocess.check_call(["git", "init", repo_path])

        yield Git(repo_path)


@pytest.mark.parametrize("cast_fn", [str, Path])
def test_init(cast_fn: Callable):
    with TemporaryDirectory() as temp_dir:
        repo_path = cast_fn(temp_dir)

        repo = Git(repo_path)
        repo.init()


def test_build_cli_args_no_args(repo: Git):
    assert repo.build_cli_args() == []


def test_build_cli_args_short_arg(repo: Git):
    assert repo.build_cli_args(v=True) == ["-v"]


def test_build_cli_args_long_arg(repo: Git):
    assert repo.build_cli_args(verbose=True) == ["--verbose"]


def test_build_cli_args_short_arg_with_value(repo: Git):
    assert repo.build_cli_args(U=20) == ["-U20"]


def test_build_cli_args_long_arg_with_value(repo: Git):
    assert repo.build_cli_args(unified=20) == ["--unified=20"]


def test_build_cli_args_long_arg_with_null_value(repo: Git):
    assert repo.build_cli_args(unified=None) == []


def test_build_cli_args_short_arg_without_value(repo: Git):
    assert repo.build_cli_args("-v") == ["-v"]


def test_build_cli_args_short_arg_is_number(repo: Git):
    assert repo.build_cli_args(_1=True) == ["-1"]
