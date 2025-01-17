#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from glob import glob
from os import path

from setuptools import find_packages
from setuptools import setup


this_directory = path.abspath(path.dirname(__file__))


with open(path.join(this_directory, 'README.rst')) as readme_file:
    long_description = readme_file.read()


setup(
    name='pytest-cython',
    version='0.3.0.dev0',
    description='A plugin for testing Cython extension modules',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Logan Page',
    author_email='page.lg@gmail.com',
    license='MIT',
    url='https://github.com/lgpage/pytest-cython',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[path.splitext(path.basename(p))[0] for p in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: https://pypi.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        # 'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],
    keywords=[
        'pytest', 'py.test', 'cython', 'doctest',
    ],
    install_requires=[
        'pytest>=4.6.0',
    ],
    entry_points={
        'pytest11': [
            'pytest_cython = pytest_cython.plugin',
        ],
    },
)
