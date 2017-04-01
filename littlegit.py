from __future__ import unicode_literals

import subprocess
import functools
import logging


__version__ = '0.1.0'


logger = logging.getLogger(__name__)


class GitError(Exception):

    __slots__ = ['cli_args', 'output', 'exit_code']

    def __init__(self, cli_args, output, exit_code):
        self.cli_args = cli_args
        self.output = output
        self.exit_code = exit_code


class Git(object):

    def __init__(self, working_dir):
        self.working_dir = working_dir

    def __getattr__(self, attr):
        cmd = attr.replace('_', '-')

        return functools.partial(self.__execute, cmd)

    def __execute(self, cmd, *args, **kwds):
        cli_args = ['git', cmd]

        for k, v in kwds.iteritems():
            if len(k) == 1:
                cli_args.append('-{}'.format(k))
            else:
                cli_args.append('--{}'.format(k.replace('_', '-')))

            if not isinstance(v, bool) and v:
                cli_args.append(v)

        cli_args.extend(args)

        logger.info(' '.join(cli_args))

        try:
            output = subprocess.check_output(
                cli_args, stderr=subprocess.STDOUT, cwd=self.working_dir
            )
        except subprocess.CalledProcessError as e:
            logger.error("Exit code %d: %s'n%s", e.returncode, e, e.output)
            raise GitError(cli_args, e.output, e.returncode)

        return output.decode('utf8')

    def init(self, **kwds):
        return self.__execute('init', self.working_dir, **kwds)
