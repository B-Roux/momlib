<!--
This is a living, breathing document that attempts to capture the style,
conventions, etc. used in this project so that those practices can be
standardized across the entire codebase.

This isn't necessarily a prescriptive document as much as it is an attempt to
enforce some kind of standard, even if that may be ever-changing.

Inconsistencies here may occur, but they must eventually be resolved.
-->

# Formatting
Use Black with a line-limit of 79 characters. It's that easy! (Note, keep
docstrings to <=72 characters). Only use ASCII characters (make use of Python's
unicode escape sequences for unicode characters).
Why? Because it's easier to enforce an existing standard than to make up a new
one. Black is not only an existing standard, it is also one with a very 
aggressive auto-formatter and can be considered generally PEP-8 compliant.
Consistency is king!

## Line Length
All line lengths (even for non-python text files such as this one) are limited
to an ABSOLUTE MAXIMUM of 79 characters per line. This is done for two reasons:
1. It keeps everything consistent
2. It allows for all of the benefits of horizontally-efficient code, such as:
    * A way of soft-forcing complex lines to be broken down
    * The ability to have two text files open side-by-side
    * The ability to read and edit code from a small terminal

## Spaces over Tabs
All code must strictly use spaces and *never include tabs*. Python requires
picking one or the other (never both), and spaces are generally considered to
be the standard since they are constant-width and more precise for alignment.
They are also PEP-8 recommended.
All modern text editors are configurable to insert spaces when the tab key is
pressed and will handle backspaces appropriately given groups of spaces - use
this instead of mashing your spacebar to death.
Also, 4 spaces. Not 2, not 8. 4.

# Typing (as in data types)
All methods, classes and modules must implement explicit type annotations
wherever necessary to make it clear to the end user what data type a certain
(for example) method requires and returns. The litmus test for this is that
the code should have no type errors or warnings on Pylance's strictest type
checking mode ("strict").

# Method Docstrings
All methods, classes and modules (except for unittest/testing) should contain a
docstring. Docstrings do not merely serve as in-code documentation for the
person who will be using the functionality given by the code, but also as an
indication to anyone who will have to refactor or maintain the code what the
code does in the first place. It is, furthermore, easier to enforce a simple
rule requiring them everywhere than trying to develop and enforce a rule for
when they are and are not needed.

The docstring format this project uses is loosely based on the Google format,
but customized to be minimal, output valid markdown, and be as compatible as
possible with VSCode's pop-up dialogues. The important changes made to the 
Google format are as follows:

1. No "Returns" field: The method name and description should adequately
    describe what the method will modify or return. An additional field for
    this information is redundant and distracting.
2. No types: The method signature is where typing documentation should go.
    This allows for the use of type checkers. (Using both docstring and
    signature type documentation is ridiculous.)
3. Hyphen-spaces instead of indentations: Since the aim of this format is to be
    markdown-compliant, hyphen-spaces are used to indicate lists of items.
4. Renamed fields: "Args," "Raises," etc. are unfriendly names. Using full,
    every-day words instead of jargon makes the documentation more accessible
    to everyone.

The format for docstrings is as follows:

```python
"""
[Short description.]

Arguments
- [arg_one]: [Short description.]
- [arg_two]: [Short description.]
- *[args]: [Short description.]
- **[kwargs]: [Short description.]

Possible Errors
- [ErrorType]: [Condition that raises it.]

Notes
- [First notes item.]
- [Second notes item.]
"""
```

In code, this will look as follows:

```python
def docstring_example(i: int, j: int = 0) -> int:
    """
    Adds `j` to `i` and returns the result.

    Arguments
    - i: The first operand.
    - j: The second operand.

    Possible Errors
    - AssertionError: If `i` is not an integer.

    Notes
    - Makes use of the integer `+` operator.
    """
    assert isinstance(i, int), 'i is not an int'
    return i+j
```

There are tentatively 4 sections in each docstring, in order:

1. Description (always required): Describe what the method does, what it 
    modifies, and what it returns. This should summarize everything someone
    using the method may need to know.
2. Arguments: Any non-implicit argument to the method should have a field
    in this section that describes what kind (*not type*) of information it
    expects. If no arguments are accepted, this entire section should be 
    omitted.
3. Possible Errors: The *exceptions* (not *warnings*) a method may raise.
    Warnings, if they are described, should be described in the "Notes"
    section. If no errors are raised, this entire section should be 
    omitted.
4. Notes: A completely optional section to make not of any details that don't
    fit in any of the other sections.

Lastly, in keeping with PEP-8, docstrings should never be more than 72
characters in length!

All of these docstring conventions are very important for consistency and thus
are enforced by the unit tests.

# Nontraditional Operator Overloads
In some cases, there exists some functionality that is expressed by an operator
symbol/convention quite well, but that operator has a different meaning in
Python. This codebase has a relatively simple rule for these:
    If there is any reason why a user may reasonably want access to the more
    traditional operator functionality, then that it what should be
    implemented. Otherwise, if there is some form of precedent, the operator
    may be nontraditionally overloaded.

## Example:
In the linalg.Matrix class, the `*` (`__mul__`) operator is usually
reserved for element-wise multiplication. This seems like a somewhat reasonable
use, so it may not be overloaded for matrix multiplication (especially because
matrix multiplication already has a dedicated operator, `@` or `__matmul__`).

On the other hand, in the same class there is an overload for the `|`
(`__or__`) operator to implement matrix augmentation. This is because the
convention exists in mathematics to express "matrix A augmented with matrix B"
as "A|B," and there is no intention of actually implementing a bit-wise or
comparison for the Matrix class.

A similar decision was made regarding overloading the `@` (`__matmul__`)
operator for Vectors' dot product, since the dot product in mathematics
is simply the matrix product of a column and row vector.

The reason why this is done is to make operations that need shorthand more
accessible. This generally improves clarity, accessibility and code
cleanliness. Nobody likes the Lovecraftian horrors that arise from multiple
nested methods.