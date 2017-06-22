from __future__ import unicode_literals

from unittest import TestCase
import os
import subprocess
import shutil

from littlegit import Git


TEST_REPO_DIR = os.path.join(os.path.dirname(__file__), '__test_repo__')


class GitTests(TestCase):

    @classmethod
    def setUpClass(cls):
        if os.path.exists(TEST_REPO_DIR):
            shutil.rmtree(TEST_REPO_DIR)

        os.makedirs(TEST_REPO_DIR)
        subprocess.check_call(['git', 'init', TEST_REPO_DIR])

    def setUp(self):
        self.git = Git(TEST_REPO_DIR)

    def test_build_cli_args_no_args(self):
        assert self.git.build_cli_args() == []

    def test_build_cli_args_short_arg(self):
        assert self.git.build_cli_args(v=True) == ['-v']

    def test_build_cli_args_long_arg(self):
        assert self.git.build_cli_args(verbose=True) == ['--verbose']

    def test_build_cli_args_short_arg_with_value(self):
        assert self.git.build_cli_args(U=20) == ['-U20']

    def test_build_cli_args_long_arg_with_value(self):
        assert self.git.build_cli_args(unified=20) == ['--unified=20']

    def test_build_cli_args_long_arg_with_null_value(self):
        assert self.git.build_cli_args(unified=None) == []

    def test_build_cli_args_short_arg_without_value(self):
        assert self.git.build_cli_args('-v') == ['-v']
