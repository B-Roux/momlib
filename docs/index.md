This library attempts to capture a limited set of advanced mathematical objects and their associated operations in the most basic and natural data types and structures available in standard Python 3, and while having no requirements other than the Python standard library.

At the moment, this library is being developed by me for my own purposes, but I hope that enough people find it useful enough that that stops being the case.

Thank you for using and supporting my project, please head over to the linked GitHub repository to report any bugs, issues or annoyances you may have with it, and I'll be sure to take your feedback into consideration! (Though do keep in mind that I may not always be able to give a satisfactory response.)

Please note that this library is currently in version 0.0.x meaning very early development. The public API may change drastically and often. As soon as version 0.1.0 is released, you should in most cases be able to expect some consistency. I hope this comes soon!

# Is this library for me?

This library has a very specific and niche function, and I will be the first to admit that - as useful as I may find it in some cases - it is not always the most appropriate option. Please use the quick guide below to determine if this library is right for your use case:

## Consider momlib if...

- You want to be able to quickly write expressive code snippets that perform common operations on common mathematical objects.
- You are using strict typing and want a mathematical library that fully supports it.
- You would like to leverage the large selection of available tools to quickly perform calculations, implement more complex algorithms, or mock up algorithms to test them before implementing them from scratch in a more appropriate way.

## But not if...

- You need high-performance and/or are dealing with very large datasets. Instead, consider a library geared towards efficiency such as NumPy.
- You need a symbolic math library or a computer algebra system (CAS). Instead, consider a library geared towards symbolic math such as SymPy.
- You need a library capable of performing secure calculations for applications such as cryptography. Instead, consider a library geared towards secure cryptographic calculations such as PySodium.
- You need a library that will perform critical calculations without errors or bugs that can lead to serious consequences if any failures are encountered - while I strive to make this library as good as it can be, I am a lone developer working on this as a side project. As such, this library comes with absolutely no guarantees, warrantees or promises. Please see the licensing agreement.

I am not affiliated with any of the products or services mentioned in the above section.

# Installing

This package can be installed from the PyPI release:

```sh
python -m pip install momlib
```

# Verifying (Version 0.0.9)

**Tarball (\*.tar.gz):**
```
SHA256: c37aec0311d90b804b21b5031ed015727bba76375dcdbdd5d2e316d0cedfb09f
MD5: 4a1e75066e82a99260f4192232b24f47
BLAKE2-256: e24c80f8f01d6142a8888a5371378837f0343927af18fce450cbdf7a69b948d6
```

**Wheel (\*.whl):**
```
SHA256: 786ae9469d1f531749051ab8d4e99de88617540664230269ee0d99d8f3764ca6
MD5: 5d9609ee2aa36dcdc5428de6e859e80b
BLAKE2-256: b811198c30a1ca92d7f0ca30411eff6bac60e259b5a9af6727d82ada264f78c1
```

If these hashes don't match the ones installed from pip, remove the files from your device immediately and open [an issue on GitHub](https://github.com/B-Roux/momlib/issues). You are responsible for reviewing any content you download and ensuring that it meets your security and safety expectations.

# Reference

- [Matrices](./reference/matrix)
- [Vectors](./reference/vector)
- [Linear Algebra](./reference/linalg)

# News

- The graph theory submodule is being indefinitely removed. I didn't like how out of place it felt in its previous implementation - perhaps in the future it will be reintroduced, but for the time being I think it is healthier for the project to address a more narrow scope of problems.

# License

BSD 3-Clause License

Copyright (c) 2023, B. Roux

All rights reserved.

Redistribution and use in source and binary forms, with or without 2modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

*THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.*
