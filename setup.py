from setuptools import setup
from .momlib import __version__ as version

setup(
    name="momlib",
    version=version,
    url="https://github.com/B-Roux/momlib",
    author="B. Roux",
    author_email="contact@momlib.org",
    description="Mathematical Object Manipulation Library",
    long_description="this is a placeholder",
    long_description_content_type="text/markdown",
    license="BSD",
    packages=["momlib"],
    test_suite="tests",
    install_requires=[],
    keywords=(
        "library graph vector matrix mathematics directed-graph "
        "shortest-paths"
    ),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
    ],
)
