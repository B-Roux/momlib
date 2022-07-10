from setuptools import setup

long_description = """
# MOMLib
## The Mathematical Object Manipulation Library for Python 3!

For regularly updated documentation, please visit the official repository at 
[github.com/B-Roux/momlib](https://github.com/B-Roux/momlib).

This project is only a few months old and absolutely still in its infancy,
however I am working on it as often as I have the time to spare by fixing
bugs that pop up and adding new features. If you have any questions,
concerns, feature requests or bug reports; the best way to notify me is 
through the [issues page](https://github.com/B-Roux/momlib/issues).

While some emails to the author email may get responses on a case-by-case
basis, the topics mentioned above will be ignored (I apologize in advance).
"""

setup(
    name="momlib",
    version="0.0.1",
    url="https://github.com/B-Roux/momlib",
    author="B. Roux",
    author_email="contact@momlib.org",
    description="Mathematical Object Manipulation Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="BSD",
    packages=[
        "momlib",
        "momlib.graph",
        "momlib.linalg",
    ],
    install_requires=[],  # must be empty
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
