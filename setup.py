#!/usr/bin/env python

from setuptools import setup

from littlegit import __version__


setup(
    name='littlegit',
    description='This is a little tiny wrapper around Git CLI',
    long_description=open("README.rst").read(),
    url='https://github.com/expobrain/littlegit',
    author='Daniele Esposti',
    author_email='daniele.esposti@gmail.com',
    py_modules=['littlegit'],
    version=__version__,
    license=open("LICENSE").read(),
    classifiers=[
        "License :: Public Domain",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Topic :: System",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries"
    ]
)
