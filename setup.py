#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-nomie",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Al Whatmough",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_nomie"],
    install_requires=[
        "singer-python>=5.0.12",
        "requests",
	"couchdb"
    ],
    entry_points="""
    [console_scripts]
    tap-nomie=tap_nomie:main
    """,
    packages=["tap_nomie"],
    package_dir={'tap_nomie': 'tap_nomie'}
    #package_data = {
    #    "schemas": ["{{cookiecutter.package_name}}/schemas/*.json"]
    #},
#    include_package_data=True,
)
