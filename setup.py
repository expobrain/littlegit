#!/usr/bin/env python

from pathlib import Path

from setuptools import setup

from littlegit import __version__

setup(
    name="littlegit",
    description="This is a little tiny wrapper around Git CLI",
    # long_description=Path("README.md").read_text(),
    # long_description_content_type="text/markdown",
    url="https://github.com/expobrain/littlegit",
    author="Daniele Esposti",
    author_email="daniele.esposti@gmail.com",
    py_modules=["littlegit"],
    version=__version__,
    license=Path("LICENSE").read_text(),
    classifiers=[
        "License :: Public Domain",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Topic :: System",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
    ],
)
