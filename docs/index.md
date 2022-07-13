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

# Licensing

All use of this library - in any form -  is subject to
    [the licensing agreement](./license). Use of this package is
    considered acknowledgement and agreement with these terms and
    conditions.

Please review this document very carefully.

# Reference

- [`momlib.linalg` - The Linear Algebra Submodule](./linalg)
- [`momlib.graph` - The Graph Theory Submodule](./graph)

# News

- The `momlib.graph` submodule is still under construction - avoid
    depending on it in cod that needs to not break in subsequent
    versions of this library!
