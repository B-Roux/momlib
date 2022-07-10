[![Python: 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)  
[![Systems: Windows, Mac, Linux](https://img.shields.io/badge/Systems-Windows%2C%20Mac%2C%20Linux-blue.svg)]()  
[![License: BSD 3-Clause](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)  
[![Code style: black](https://img.shields.io/badge/Style-Black%2C%20PEP--8-blue.svg)](https://github.com/psf/black)  

[![Unit Tests](https://github.com/B-Roux/momlib/actions/workflows/tests.yml/badge.svg)](https://github.com/B-Roux/momlib/actions/workflows/tests.yml) 
[![PyPI Release Test](https://github.com/B-Roux/momlib/actions/workflows/pypi-release-test.yml/badge.svg?branch=master)](https://github.com/B-Roux/momlib/actions/workflows/pypi-release-test.yml)  

# Mathematical<br>Object<br>Manipulation<br>Library

This package attempts to capture a limited set of advanced mathematical
    objects and their associated operations in the most basic and
    natural data types and structures available in standard Python 3,
    and while having no requirements other than the Python standard
    library.

At the moment, this package is being developed by me for my own
    purposes, but I hope that enough people find it useful enough that
    that stops being the case. Thank you for using and supporting my
    project!

Please note that this package is currently in version 0.0.x meaning
    very early development. The public API may change drastically and
    often. As soon as version 0.1.0 is released, you should in most
    cases be able to expect some consistency. I hope this comes soon!
    
# Installing

This package can be installed from the PyPI release:

```sh
pip install momlib
```

# Documentation
## Guide
The guide is not currently available as the public API has not been 
completely defined. This will change upon the release of version 
`0.1.x`.

## API
* [Linear Algebra](./docs/api/linalg)
  * [Matrix](./docs/api/linalg/matrix.md)
  * [Vector](./docs/api/linalg/vector.md)
  * [Linear algebra tools](./docs/api/linalg/tools.md)
* [Graph Theory](./docs/api/graph)
  * [Graph](./docs/api/graph/graph.md)
  * [Directed graph](./docs/api/graph/digraph.md)
  * [Graph theory tools](./docs/api/graph/tools.md)

# Licensing
The official (and only!) licensing agreement for using this project can
    be found in [the licensing file](./LICENSE.md). It's pretty simple:
    you can privately or commercially modify, distribute or use this
    software - for free (gratis *and* libre) - under the exact terms
    detailed by this license. Be aware that I am not liable for any use
    of this software, nor do I provide it with any warrantees or
    guarantees.

# Code Standards and Design
I aim to keep my code well-formatted and to a tight standard. While this
    standard is constantly evolving and may get outdated often, I 
    attempt to capture its most recent form in 
    [this document](./design/code_conventions.md).
    
# Current Work
I am currently mostly working on the graph theory submodule.
    Until this is fully fleshed out, work on other submodules will be
    minimal.
