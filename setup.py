#!/usr/bin/env python
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "recsys_func",
    version = "0.0.1",
    author = "Kim Falk",
    description = (""),
    license = "GNU",
    keywords = "example recsys",
    packages=['similarity', 'tests'],
    long_description=read('README.md'),
)