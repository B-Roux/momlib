from setuptools import setup
from .momlib import __version__ as version

with open("./README.md", "r") as f:
    long_description = f.read()

setup(
    name="momlib",
    version=version,
    author="B. Roux",
    package_dir={"": "momlib"},
    packages=[
        "momlib",
    ],
    description="Mathematical Object Manipulation Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://momlib.pages.b-roux.com/",
    project_urls={
        "Bug Tracker": "https://github.com/B-Roux/momlib/issues",
    },
    license="BSD (3-Clause)",
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
