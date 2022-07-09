# Matrix Object API

Expresses the mathematical notion of a rational-valued matrix in
    native Python datastructures and datatypes while providing an
    assortment of tools to perform basic matrix manipulations.

`Matrix` objects are considered non-mutable, which means that for
    the life of an object it cannot be meaningfully modified[^1].
    Matrices are, therefore, hashable (using
    `hash(matrix_instance)`).

[^1]: If you need to modify a `Matrix`, look into the
    `matrix_instance.elements` property.

## Contents

- [cat](#matrixcat)
- [get\_slice](#matrixget\_slice)
- [limit\_denominator](#matrixlimit\_denominator)

---

## Matrix.cat
```python
(self, other: 'Matrix', horizontally: 'bool' = True) -> 'Matrix'
```
Concatenates the rows of this matrix with the rows of the
    `other` matrix.

Arguments
- other: The right-hand side rows to append.
- horizontally: Whether to concatenate the matrices horizontally
    (when true) or vertically (when false).
    Optional, defaults to true.

Possible Errors
- DimensionMismatchError: If the two matrices have unequal shape
    dimensions perpendicular to the direction of concatenation.

---

## Matrix.get\_slice
```python
(self, rows: 'tuple[int | EllipsisType, int | EllipsisType] | EllipsisType | int' = Ellipsis, cols: 'tuple[int | EllipsisType, int | EllipsisType] | EllipsisType | int' = Ellipsis) -> 'Matrix'
```
Crops unselected rows and columns from this matrix and
    returns the result.

Arguments
- rows: The rows to keep. If a tuple, this specifies the
    starting coordinate (inclusive) followed by the ending
    coordinate (exclusive). If an integer, this specifies a
    single row. If ellipses, this specifies all rows.
    Optional, defaults to ellipses. Ellipses signify either
    "from the beginning" or "to the end" inside tuples, for
    positions 0 and 1, respectively.
- cols: The columns to keep. If a tuple, this specifies the
    starting coordinate (inclusive) followed by the ending
    coordinate (exclusive). If an integer, this specifies a
    single column. If ellipses, this specifies all columns.
    Optional, defaults to ellipses. Ellipses signify either
    "from the beginning" or "to the end" inside tuples, for
    positions 0 and 1, respectively.

Possible Errors
- IndexError: If the slice would create a matrix with zero
    elements.

---

## Matrix.limit\_denominator
```python
(self, max_denominator: 'int') -> 'Matrix'
```
Limits the denominator of all `Fraction` objects in this
    matrix to some upper bound.

Arguments
- max_denominator: The largest allowed denominator.

Possible Errors
- ZeroDivisionError: If `max_denominator` is 0.

<!--This file has been automatically generated-->
