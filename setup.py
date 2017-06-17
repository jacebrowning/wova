#!/usr/bin/env python

"""Setup script for the package."""

import os
import sys
import setuptools


PACKAGE_NAME = 'wova'
MINIMUM_PYTHON_VERSION = '2.6'


def check_python_version():
    """Exit when the Python version is too low."""
    if sys.version < MINIMUM_PYTHON_VERSION:
        sys.exit("Python {0}+ is required.".format(MINIMUM_PYTHON_VERSION))


def read_package_variable(key, filename='__init__.py'):
    """Read the value of a variable from the package without importing."""
    module_path = os.path.join(PACKAGE_NAME, filename)
    with open(module_path) as module:
        for line in module:
            parts = line.strip().split(' ', 2)
            if parts[:-1] == [key, '=']:
                return parts[-1].strip("'")
    sys.exit("'{0}' not found in '{1}'".format(key, module_path))


def build_description():
    """Build a description for the project from documentation files."""
    try:
        readme = open("README.rst").read()
        changelog = open("CHANGELOG.rst").read()
    except IOError:
        return "<placeholder>"
    else:
        return readme + '\n' + changelog


check_python_version()

setuptools.setup(
    name=read_package_variable('__project__'),
    version=read_package_variable('__version__'),

    description="Oliver Rice's personal python library",
    url='https://github.com/olirice/https://github.com/olirice/wova.git',
    author='Oliver Rice',
    author_email='oliver@oliverrice.com',

    packages=setuptools.find_packages(),

    long_description=build_description(),
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
	'Programming Language :: Python :: 2.7',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.3',
	'Programming Language :: Python :: 3.4',
	'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6',
	"Programming Language :: Python :: Implementation :: CPython"
	"Programming Language :: Python :: Implementation :: PyPy"
    ],

    install_requires=[
        "six ~= 1.10.0",
        "future ~= 0.16.0",
    ]
)
