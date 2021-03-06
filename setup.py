#!/usr/bin/env python

# Original author listed was Scott Hansen. This is a tabview fork for github.com/interrogator/buzz

from distutils.core import setup

try:
    # Setuptools only needed for building the package
    import setuptools  # noqa
except ImportError:
    pass

setup(
    name="tabview",
    version="1.4.5",
    description="A curses command-line CSV and list (tabular data) viewer",
    long_description=open("README.rst", "rb").read().decode("utf-8"),
    author="Danny McDonald",
    author_email="mcddjx@gmail.com",
    url="https://github.com/interrogator/tabview",
    download_url="https://github.com/interrogator/tabview",
    packages=["tabview"],
    package_data={"tabview": ["README.rst"]},
    data_files=[("share/doc/tabview", ["README.rst", "LICENSE.txt", "CHANGELOG.rst"])],
    test_suite="test/test_tabview.py",
    license="MIT",
    install_requires=["colorama"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Console :: Curses",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Utilities",
    ],
    keywords=(
        "data spreadsheet view viewer console " "curses csv comma separated values"
    ),
)
