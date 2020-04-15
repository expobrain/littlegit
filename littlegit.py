import functools
import logging
import subprocess

__version__ = "0.2.0b4"


logger = logging.getLogger(__name__)


class GitError(Exception):

    __slots__ = ["cli_args", "output", "exit_code"]

    def __init__(self, cli_args, output, exit_code):
        self.cli_args = cli_args
        self.output = output
        self.exit_code = exit_code


class Git(object):
    def __init__(self, working_dir):
        self.working_dir = working_dir

    def __getattr__(self, attr):
        cmd = attr.replace("_", "-")

        return functools.partial(self.__execute, cmd)

    def build_cli_args(self, *args, **kwds):
        cli_args = []

        for k, v in kwds.items():
            short_arg = len(k) == 1

            if short_arg:
                arg = "-{}".format(k)
            else:
                arg = "--{}".format(k.replace("_", "-"))

            if isinstance(v, bool):
                cli_args.append(arg)
            elif v:
                if short_arg:
                    cli_args.append("{}{}".format(arg, v))
                else:
                    cli_args.append("{}={}".format(arg, v))

        cli_args.extend(args)

        return cli_args

    def __execute(self, cmd, *args, **kwds):
        cli_cmd = ["git", cmd] + self.build_cli_args(*args, **kwds)

        logger.info(" ".join(cli_cmd))

        try:
            output = subprocess.check_output(
                cli_cmd, stderr=subprocess.STDOUT, cwd=self.working_dir
            )
        except subprocess.CalledProcessError as e:
            logger.error("Exit code %d: %s'n%s", e.returncode, e, e.output)
            raise GitError(cli_cmd, e.output, e.returncode)

        return output.decode("utf8")

    def init(self, **kwds):
        return self.__execute("init", self.working_dir, **kwds)
