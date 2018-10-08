# -*- coding: utf-8 -*-
"""sqla-filters-json setup file."""
import os
from typing import List
from setuptools import (
    setup,
    find_packages,
)

NAME: str = 'sqla-filters-json'
VERSION: str = '0.0.1'
DESCRIPTION: str = 'JSON parser for sqla-filters.'

def get_requirements() -> List[str]:
    """Return the requirements as a list of string."""
    requirements_path = os.path.join(
        os.path.dirname(__file__), 'requirements.txt'
    )
    with open(requirements_path) as f:
        return f.read().split()

def read(file_path: str):
    """Simply return the content of a file."""
    with open(file_path) as f:
        return f.read()

REQUIRE: List[str] = get_requirements()

DEV_REQUIRE: List[str] = [
    'pylint',
    'pep8',
    'autopep8',
    'ipython',
    'mypy',
    'pytest',
    'rope',
    'sphinx',
    'twine'
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read(os.path.join(os.path.dirname(__file__), 'README.md')),
    long_description_content_type='text/markdown',
    url='https://github.com/MarcAureleCoste/sqla-filters-json',

    author='Marc-Aurele Coste',

    license='MIT',
    zip_safe=False,

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    install_requires=REQUIRE,
    packages=(
        'sqla_filters.parser.json',
    ),
    package_dir={'': 'src'},

    entry_points={},

    tests_require=DEV_REQUIRE,
    extras_require={
        'dev': DEV_REQUIRE
    }
)