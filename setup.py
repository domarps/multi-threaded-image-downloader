# -*- coding: utf-8 -*-

# Learn more: # add link

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='multithreaded_image_downloads',
    version='0.0.0',
    description='--BLANK--',
    long_description=readme,
    author='Pramod Srinivasan',
    author_email='spmd92@gmail.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

