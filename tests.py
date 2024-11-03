import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

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


@pytest.mark.parametrize(
    "args, kwds, expected",
    [
        [[], {}, []],
        [[], {"v": True}, ["-v"]],
        [[], {"verbose": True}, ["--verbose"]],
        [[], {"U": 20}, ["-U20"]],
        [[], {"unified": 20}, ["--unified=20"]],
        [[], {"unified": None}, []],
        [[], {"_1": True}, ["-1"]],
        [["HEAD"], {}, ["HEAD"]],
    ],
)
def test_build_cli_args(repo: Git, args: list, kwds: dict, expected: list[str]):
    assert repo.build_cli_args() == []
