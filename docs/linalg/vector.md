# Vector Object Instance Methods
## Contents

- [\_\_init\_\_](./#\_\_init\_\_)
- [\_\_len\_\_](./#\_\_len\_\_)
- [\_\_getitem\_\_](./#\_\_getitem\_\_)
- [\_\_iter\_\_](./#\_\_iter\_\_)
- [\_\_next\_\_](./#\_\_next\_\_)
- [\_\_str\_\_](./#\_\_str\_\_)
- [\_\_repr\_\_](./#\_\_repr\_\_)
- [\_\_matmul\_\_](./#\_\_matmul\_\_)
- [\_\_mul\_\_](./#\_\_mul\_\_)
- [\_\_rmul\_\_](./#\_\_rmul\_\_)
- [\_\_truediv\_\_](./#\_\_truediv\_\_)
- [\_\_rtruediv\_\_](./#\_\_rtruediv\_\_)
- [\_\_add\_\_](./#\_\_add\_\_)
- [\_\_radd\_\_](./#\_\_radd\_\_)
- [\_\_sub\_\_](./#\_\_sub\_\_)
- [\_\_rsub\_\_](./#\_\_rsub\_\_)
- [\_\_neg\_\_](./#\_\_neg\_\_)
- [\_\_eq\_\_](./#\_\_eq\_\_)
- [\_\_hash\_\_](./#\_\_hash\_\_)
- [cat](./#cat)
- [get\_slice](./#get\_slice)
- [limit\_denominator](./#limit\_denominator)

---

# \_\_init\_\_

```python
(self, initializer: 'Iterable[float | Fraction]') -> 'None'
```

Initializes a new instance of the `Vector` class.

Arguments
- initializer: An iterable that will be used to construct the
    vector.

Possible Errors
- ValueError: If the initializer has no elements.

---

# \_\_len\_\_

```python
(self) -> 'int'
```

Returns the total number of elements in this vector.

---

# \_\_getitem\_\_

```python
(self, key: 'int') -> 'Fraction'
```

Returns a copy of the item at a given position.

Arguments
- key: The 0-indexed position of the desired element.

Possible Errors
- IndexError: If the key index is out of bounds.

---

# \_\_iter\_\_

```python
(self) -> 'Vector'
```

Initializes this vector for iteration using the `\_\_next\_\_`
method.

---

# \_\_next\_\_

```python
(self) -> 'Fraction'
```

Returns the next item in a row-wise traversal of this vector
    if the `\_\_iter\_\_` method has been used to initialize
    iteration.

Possible Errors
- RuntimeError: If iteration was not properly initialized.

Notes
- Raises `StopIteration` when all items have been iterated over.

---

# \_\_str\_\_

```python
(self) -> 'str'
```

Returns a "pretty" string representation of this vector.

---

# \_\_repr\_\_

```python
(self) -> 'str'
```

Returns a reproduction string representation of this vector.

---

# \_\_matmul\_\_

```python
(self, other: 'Vector') -> 'Fraction'
```

Calculates the dot product of this and another vector.

Arguments
- other: The right-hand-side operand to dot multiplication.

Possible Errors
- DimensionMismatchError: If the two vectors have different
    lengths.

Notes
- To calculate the element-wise product of two vectors, use the
    `\_\_mul\_\_` (asterisk) operator.

---

# \_\_mul\_\_

```python
(self, other: 'Vector | float | Fraction') -> 'Vector'
```

Calculates the element-wise product of this vector and either
    another vector or a single number.

Arguments
- other: The left-hand-side operand.

Possible Errors
- DimensionMismatchError: If `other` is a Vector and does not
    have the required shape.

Notes
- To calculate the dot product of two matrices, use the
    `\_\_matmul\_\_` (at-sign) operator.

---

# \_\_rmul\_\_

```python
(self, other: 'float | Fraction') -> 'Vector'
```

Calculates the element-wise product of this vector and either
    another vector or a single number (if this vector is the
    right-hand-side operand).

Arguments
- other: The right-hand-side operand.

Possible Errors
- DimensionMismatchError: If `other` is a Vector and does not
    have the required shape.

Notes
- To calculate the dot product of two matrices, use the
    `\_\_matmul\_\_` (at-sign) operator.

---

# \_\_truediv\_\_

```python
(self, other: 'Vector | float | Fraction') -> 'Vector'
```

Calculates the element-wise quotient of this vector and either
    another vector or a single number.

Arguments
- other: The left-hand-side operand.

Possible Errors
- DimensionMismatchError: If `other` is a Vector and does not
    have the required shape.
- ZeroDivisionError: If `other` is zero, or is a vector that
    contains a zero anywhere.

---

# \_\_rtruediv\_\_

```python
(self, other: 'float | Fraction') -> 'Vector'
```

Calculates the element-wise quotient of this vector and either
    another vector or a single number (if this vector is the
    right-hand-side operand).

Arguments
- other: The right-hand-side operand.

Possible Errors
- DimensionMismatchError: If `other` is a Vector and does not
    have the required shape.
- ZeroDivisionError: If `other` is zero, or is a vector that
    contains a zero anywhere.

---

# \_\_add\_\_

```python
(self, other: 'Vector | float | Fraction') -> 'Vector'
```

Calculates the element-wise sum of this vector and either
    another vector or a single number.

Arguments
- other: The left-hand-side operand.

Possible Errors
- DimensionMismatchError: If `other` is a Vector and does not
    have the required shape.

---

# \_\_radd\_\_

```python
(self, other: 'float | Fraction') -> 'Vector'
```

Calculates the element-wise sum of this vector and either
    another vector or a single number (if this vector is the
    right-hand-side operand).

Arguments
- other: The right-hand-side operand.

Possible Errors
- DimensionMismatchError: If `other` is a Vector and does not
    have the required shape.

---

# \_\_sub\_\_

```python
(self, other: 'Vector | float | Fraction') -> 'Vector'
```

Calculates the element-wise difference of this vector and either
    another vector or a single number.

Arguments
- other: The left-hand-side operand.

Possible Errors
- DimensionMismatchError: If `other` is a Vector and does not
    have the required shape.

---

# \_\_rsub\_\_

```python
(self, other: 'float | Fraction') -> 'Vector'
```

Calculates the element-wise difference of this vector and either
    another vector or a single number (if this vector is the
    right-hand-side operand).

Arguments
- other: The right-hand-side operand.

Possible Errors
- DimensionMismatchError: If `other` is a Vector and does not
    have the required shape.

---

# \_\_neg\_\_

```python
(self) -> 'Vector'
```

Calculates the element-wise negation of this vector.

---

# \_\_eq\_\_

```python
(self, other: 'Any') -> 'bool'
```

Compares this vector to an object, returns true if and only
    if the right-hand side is a vector with the same length
    as this vector, such that every element in this vector is
    equal to every corresponding element in the `other` vector
    (otherwise returns false).

Arguments
- other: The object this vector is to be compared to.

---

# \_\_hash\_\_

```python
(self) -> 'int'
```

Returns the hash of this vector.

---

# cat

```python
(self, other: 'Vector | float | Fraction') -> 'Vector'
```

Concatenates the elements of this vector with the elements of
    the `other` vector.

Arguments
- other: The vector to append to this vector.

Possible Errors
- DimensionMismatchError: If the two vectors have unequal
    lengths.

---

# get\_slice

```python
(self, items: 'tuple[int | EllipsisType, int | EllipsisType]') -> 'Vector'
```

Crops unselected elements from this vector and returns the
    result.

Arguments
- items: The range of elements to keep. This specifies the
    starting coordinate (inclusive) followed by the ending
    coordinate (exclusive). Ellipses signify either "from the
    beginning" or "to the end" inside tuples, for positions 0
    and 1, respectively.

Possible Errors
- IndexError: If the slice would create a vector with zero
    elements.

---

# limit\_denominator

```python
(self, max_denominator: 'int') -> 'Vector'
```

Limits the denominator of all `Fraction` objects in this
    vector to some upper bound.

Arguments
- max\_denominator: The largest allowed denominator.

Possible Errors
- ZeroDivisionError: If `max\_denominator` is 0.
