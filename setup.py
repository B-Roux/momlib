from setuptools import setup

long_description = """
# momlub
## The Mathematical Object Manipulation Library for Python 3!

Please note that documentation for this package is not maintained on the
PyPI repository.
Please use the following links instead:

- [www.momlib.org](https://www.momlib.org/) for the website (and tutorials!)
- [github.com/B-Roux/momlib](https://github.com/B-Roux/momlib) for the repository
- [github.com/B-Roux/momlib/issues](https://github.com/B-Roux/momlib/issues) for bug reports, feature requests, questions, concerns, etc.

Please note that the email associated with this package may not reply to messages. Please use the issue page if you need a reply.
"""

setup(
    name="momlib",
    version="0.0.2",
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
