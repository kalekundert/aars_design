#!/usr/bin/env python3
# encoding: utf-8

from setuptools import setup

with open('README.rst') as file:
    readme = file.read()

setup(
    name='aars_design',
    version='0.0.0',
    author='Kale Kundert',
    long_description=readme,
    packages=[
        'aars_design',
    ],
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
        ],
    },
    include_package_data=True,
)
