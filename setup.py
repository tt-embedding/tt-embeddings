
from setuptools import setup

setup(
    name='t3nsor',
    version='1.0',
    description='TT decomposition on Pytorch',
    author='Anonymous',
    author_email='-',
    packages=['t3nsor'],  # same as name
    install_requires=['numpy', 'sympy', 'scipy'],  # external packages as dependencies
)
