"""
Mathematical
Object
Manipulation
Library

This package attempts to capture a limited set of advanced mathematical
    objects and their associated operations in the most basic and
    natural data types and structures available in standard Python 3,
    and while having no requirements other than the Python standard
    library.

At the moment, this package is being developed by me for my own
    purposes, but I hope that enough people find it useful enough that
    that stops being the case.

Thank you for using and supporting my project, please head over to the
    linked GitHub repository to report any bugs, issues or annoyances
    you may have with it, and I'll be sure to take your feedback into
    consideration! (Though do keep in mind that I may not always be able
    to give a satisfactory response.)

Please note that this package is currently in version 0.0.x meaning
    very early development. The public API may change drastically and
    often. As soon as version 0.1.0 is released, you should in most
    cases be able to expect some consistency. I hope this comes soon!
"""

__all__ = (
    "linalg",
    "graph",
)

from . import linalg
from . import graph
