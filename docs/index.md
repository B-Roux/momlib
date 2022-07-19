This library attempts to capture a limited set of advanced mathematical
    objects and their associated operations in the most basic and
    natural data types and structures available in standard Python 3,
    and while having no requirements other than the Python standard
    library.

At the moment, this library is being developed by me for my own
    purposes, but I hope that enough people find it useful enough that
    that stops being the case.

Thank you for using and supporting my project, please head over to the
    linked GitHub repository to report any bugs, issues or annoyances
    you may have with it, and I'll be sure to take your feedback into
    consideration! (Though do keep in mind that I may not always be able
    to give a satisfactory response.)

Please note that this library is currently in version 0.0.x meaning
    very early development. The public API may change drastically and
    often. As soon as version 0.1.0 is released, you should in most
    cases be able to expect some consistency. I hope this comes soon!

# Is this library for me?

This library has a very specific and niche function, and I will be the
    first to admit that - as useful as I may find it in some cases - 
    it is not always the most appropriate option. Please use the
    quick guide below to determine if this library is right for your
    use case:

## Consider momlib if...

- You want to be able to quickly write expressive code snippets that
    perform common operations on common mathematical objects.
- You are using strict typing and want a mathematical library that
    fully supports it.
- You would like to leverage the large selection of available tools
    to quickly perform calculations, implement more complex algorithms,
    or mock up algorithms to test them before implementing them from
    scratch in a more appropriate way.

## But not if...

- You need high-performance and/or are dealing with very large datasets.
    Instead, consider a library geared towards efficiency such as
    NumPy.
- You need a symbolic math library or a computer algebra system (CAS).
    Instead, consider a library geared towards symbolic math such as
    SymPy.
- You need a library capable of performing secure calculations for
    applications such as cryptography. Instead, consider a library
    geared towards secure cryptographic calculations such as PySodium.
- You need a library that will perform critical calculations without
    errors or bugs that can lead to serious consequences if any failures
    are encountered - while I strive to make this library as good as it
    can be, I am a lone developer working on this as a side project.
    As such, this library comes with absolutely no guarantees,
    warrantees or promises. Please see the licensing agreement.

I am not affiliated with any of the products or services mentioned in
    the above section.

# Installing

This package can be installed from the PyPI release:

```sh
python -m pip install momlib
```

# Reference

- [`momlib.linalg` - The Linear Algebra Submodule](./linalg)
- [`momlib.graph` - The Graph Theory Submodule](./graph)

# News

- The `momlib.graph` submodule is still under construction - avoid
    depending on it in cod that needs to not break in subsequent
    versions of this library!
- I am planning on moving my development environment for this project
    to Debian, starting whenever Python 3.10 is made available on the 
    Debian repositories. This will ensure that the most up-to-date
    version of this library will be compatible with the most recent
    Python release on Debian, as opposed to ensuring compatibility
    with the most recent release of Python as a whole.

# License

BSD 3-Clause License

Copyright (c) 2022, B. Roux

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

*THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.*
