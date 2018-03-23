#!/usr/bin/env python

import os
import re
import sys

from codecs import open

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = ['project']

requires = []
test_requirements = ['pytest>=2.8.0', 'pytest-httpbin==0.0.7', 'pytest-cov']

with open('project/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

readme_file = 'README.md'
if os.path.isfile('README-pypi.md'):
    readme_file = 'README-pypi.md'
with open(readme_file, 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.md', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name='project',
    version=version,
    description='Python Basic Project.',
    long_description=readme + '\n\n' + history,
    author='Peter Salas',
    author_email='psalas@gmail.com',
    url='http://github.com/gradeawarrior',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE'], 'project': ['*.pem']},
    package_dir={'project': 'project'},
    include_package_data=True,
    install_requires=requires,
    license='Apache 2.0',
    keywords=['testing', 'project'],
    zip_safe=False,

    # If you have a script that you want to make available on cmd-line
    scripts=['hello-world'],

    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ),
    cmdclass={'test': PyTest},
    tests_require=test_requirements,
)
