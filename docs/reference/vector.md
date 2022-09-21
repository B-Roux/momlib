# Vector Object Instance Methods

Expresses the mathematical notion of a rational-valued Vector in
    native Python datastructures and datatypes while providing an
    assortment of tools to perform basic vector manipulations.

`Vector` objects are considered non-mutable, which means that for
    the life of an object it cannot be meaningfully modified[^1].
    Vectors are, therefore, hashable (using
    `hash(vector_instance)`).

[^1]: If you need to modify a `Vector`, look into the
    `vector_instance.elements` property.

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
- [\_\_hash\_\_](#__hash__)
- [concat](#concat)

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
(self, key: 'int | slice') -> 'Fraction | Vector'
```

Returns a copy of the items at given positions.

Arguments
- key: The 0-indexed position of the desired elements.

Possible Errors
- IndexError: If the slice would create a vector with zero
    elements, or if an integer index is out of bounds.

---

# \_\_iter\_\_

```python
(self) -> 'Iterator[Fraction]'
```

Returns an iterator over the items of this vector.

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
    `__mul__` (asterisk) operator.

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
    `__matmul__` (at-sign) operator.

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
    `__matmul__` (at-sign) operator.

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

# concat

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

<!--this file has been automatically generated-->
