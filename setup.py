# coding: utf-8

"""
setup package
"""  # noqa: E501

from pathlib import Path
import setuptools
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name='getsecure',
    version='0.0.4',
    packages=[''],
    url='https://github.com/maratsh/getsecure',
    license='MIT',
    author='maratsh',
    author_email='ya@maratsh.ru',
    description='Utility for securing expiring links',
    long_description_content_type='text/markdown',
    long_description=long_description
)
