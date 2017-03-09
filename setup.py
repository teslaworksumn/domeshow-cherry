#!/usr/bin/env python3

from setuptools import setup

setup(name='domeshow-cherry',
      version='0.2',
      description='The Doooooooooooooooooooooooooooooooooome Controller',
      author='Tesla Works',
      license='MIT',
      packages=['src'],
      install_requires=[
        'Rx',
        'pyserial'
      ]
     )
