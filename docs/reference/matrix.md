# Matrix Object Instance Methods

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

- [\_\_init\_\_](#__init__)
- [\_\_len\_\_](#__len__)
- [\_\_getitem\_\_](#__getitem__)
- [\_\_iter\_\_](#__iter__)
- [\_\_str\_\_](#__str__)
- [\_\_repr\_\_](#__repr__)
- [\_\_matmul\_\_](#__matmul__)
- [\_\_mul\_\_](#__mul__)
- [\_\_rmul\_\_](#__rmul__)
- [\_\_truediv\_\_](#__truediv__)
- [\_\_rtruediv\_\_](#__rtruediv__)
- [\_\_add\_\_](#__add__)
- [\_\_radd\_\_](#__radd__)
- [\_\_sub\_\_](#__sub__)
- [\_\_rsub\_\_](#__rsub__)
- [\_\_neg\_\_](#__neg__)
- [\_\_eq\_\_](#__eq__)
- [\_\_or\_\_](#__or__)
- [\_\_hash\_\_](#__hash__)

---

# \_\_init\_\_

```python
(self, initializer: 'Iterable[Iterable[float | Fraction]]') -> 'None'
```

Initializes a new instance of the `Matrix` class.

Arguments
- initializer: A 2D iterable that will be used to construct the
    matrix.

Possible Errors
- ValueError: If the initializer has no elements, or if the
    initializer is jagged (not rectangular).

---

# \_\_len\_\_

```python
(self) -> 'int'
```

Returns the total number of elements in this matrix.

---

# \_\_getitem\_\_

```python
(self, key: 'tuple[int | slice, int | slice]') -> 'Fraction | Matrix'
```

Returns the items at specified coordinates in this matrix.

Arguments
- key: The 0-indexed row-column coordinates of the desired
    elements.

Possible Errors
- IndexError: If the slice would create a matrix with zero
    elements, or if an integer index is out of bounds.

---

# \_\_iter\_\_

```python
(self) -> 'Iterator[tuple[Fraction, ...]]'
```

Returns an iterator over the rows of this matrix.

---

# \_\_str\_\_

```python
(self) -> 'str'
```

Returns a "pretty" string representation of this matrix.

---

# \_\_repr\_\_

```python
(self) -> 'str'
```

Returns a reproduction string representation of this matrix.

Notes
- Assuming all relevant libraries have been imported, the
    reproduction string can be run as valid Python to create
    an exact copy of this matrix.

---

# \_\_matmul\_\_

```python
(self, other: 'Matrix') -> 'Matrix'
```

Returns the matrix product of this and another
    matrix.

Arguments
- other: The right-hand-side operand to matrix multiplication.

Possible Errors
- DimensionMismatchError: If the column count of `self` does not
    match the row count of `other`.

---

# \_\_mul\_\_

```python
(self, other: 'Matrix | float | Fraction') -> 'Matrix'
```

Calculates the element-wise product of this matrix and either
    another matrix or a single number.

Arguments
- other: The left-hand-side operand.

Possible Errors
- DimensionMismatchError: If `other` is a Matrix and does not
    have the required shape.

Notes
- To calculate the matrix product of two matrices, use the
    `__matmul__` (at-sign) operator.

---

# \_\_rmul\_\_

```python
(self, other: 'float | Fraction') -> 'Matrix'
```

Calculates the element-wise product of this matrix and either
    another matrix or a single number (if this matrix is the
    right-hand-side operand).

Arguments
- other: The right-hand-side operand.

Possible Errors
- DimensionMismatchError: If `other` is a Matrix and does not
    have the required shape.

Notes
- To calculate the matrix product of two matrices, use the
    `__matmul__` (at-sign) operator.

---

# \_\_truediv\_\_

```python
(self, other: 'Matrix | float | Fraction') -> 'Matrix'
```

Calculates the element-wise quotient of this matrix and either
    another matrix or a single number.

Arguments
- other: The left-hand-side operand.

Possible Errors
- DimensionMismatchError: If `other` is a Matrix and does not
    have the required shape.
- ZeroDivisionError: If `other` is zero, or is a matrix that
    contains a zero anywhere.

---

# \_\_rtruediv\_\_

```python
(self, other: 'float | Fraction') -> 'Matrix'
```

Calculates the element-wise quotient of this matrix and either
    another matrix or a single number (if this matrix is the
    right-hand-side operand).

Arguments
- other: The right-hand-side operand.

Possible Errors
- DimensionMismatchError: If `other` is a Matrix and does not
    have the required shape.
- ZeroDivisionError: If `other` is zero, or is a matrix that
    contains a zero anywhere.

---

# \_\_add\_\_

```python
(self, other: 'Matrix | float | Fraction') -> 'Matrix'
```

Calculates the element-wise sum of this matrix and either
    another matrix or a single number.

Arguments
- other: The left-hand-side operand.

Possible Errors
- DimensionMismatchError: If `other` is a Matrix and does not
    have the required shape.

---

# \_\_radd\_\_

```python
(self, other: 'float | Fraction') -> 'Matrix'
```

Calculates the element-wise sum of this matrix and either
    another matrix or a single number (if this matrix is the
    right-hand-side operand).

Arguments
- other: The right-hand-side operand.

Possible Errors
- DimensionMismatchError: If `other` is a Matrix and does not
    have the required shape.

---

# \_\_sub\_\_

```python
(self, other: 'Matrix | float | Fraction') -> 'Matrix'
```

Calculates the element-wise difference of this matrix and either
    another matrix or a single number.

Arguments
- other: The left-hand-side operand.

Possible Errors
- DimensionMismatchError: If `other` is a Matrix and does not
    have the required shape.

---

# \_\_rsub\_\_

```python
(self, other: 'float | Fraction') -> 'Matrix'
```

Calculates the element-wise difference of this matrix and either
    another matrix or a single number (if this matrix is the
    right-hand-side operand).

Arguments
- other: The right-hand-side operand.

Possible Errors
- DimensionMismatchError: If `other` is a Matrix and does not
    have the required shape.

---

# \_\_neg\_\_

```python
(self) -> 'Matrix'
```

Calculates the element-wise negation of this matrix.

---

# \_\_eq\_\_

```python
(self, other: 'Any') -> 'bool'
```

Compares this matrix to an object, returns `True` if and only
    if the right-hand side is a matrix with the same dimensions
    as this matrix, such that every element in this matrix is
    equal to every corresponding element in the `other` matrix
    (otherwise returns `False`).

Arguments
- other: The object this vector is to be compared to.

---

# \_\_or\_\_

```python
(self, other: 'Matrix') -> 'Matrix'
```

Augments the rows of this matrix with the rows of the
    `other` matrix.

Arguments
- other: The right-hand side rows to append.

Possible Errors
- DimensionMismatchError: If the two matrices have unequal row
    counts.

---

# \_\_hash\_\_

```python
(self) -> 'int'
```

Returns the hash of this matrix.

<!--this file has been automatically generated-->
