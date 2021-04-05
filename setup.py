# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "jobbing"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Aprende tu mismo API",
    author_email="soporte@jaliscoconempleo.org",
    url="",
    keywords=["Swagger", "Aprende tu mismo API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['jobbing=jobbing.__main__:main']},
    long_description="""\
    Application created to provide training courses
    """
)
