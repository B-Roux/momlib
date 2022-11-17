from setuptools import setup
from .momlib import __version__ as version

with open("./README.md", "r") as f:
    long_description = f.read()

setup(
    name="momlib",
    version=version,
    url="https://momlib.pages.b-roux.com/",
    author="B. Roux",
    description="Mathematical Object Manipulation Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="BSD (3-Clause)",
    packages=[
        "momlib",
    ],
    keywords=[
        "library",
        "vector",
        "matrix",
        "mathematics",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
