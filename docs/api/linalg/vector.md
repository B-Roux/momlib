# Vector Object API

Expresses the mathematical notion of a Vector in **R** in native
    Python datastructures and datatypes while providing an
    assortment of tools to perform basic vector manipulations.

`Vector` objects are considered non-mutable, which means that for
    the life of an object it cannot be meaningfully modified[^1].
    Vectors are, therefore, hashable (using
    `hash(vector_instance)`).

[^1]: If you need to modify a `Vector`, look into the
    `vector_instance.elements` property.

## Contents

- [cat](#vectorcat)
- [get\_slice](#vectorget\_slice)
- [limit\_denominator](#vectorlimit\_denominator)

---

## Vector.cat
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

## Vector.get\_slice
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

## Vector.limit\_denominator
```python
(self, max_denominator: 'int') -> 'Vector'
```
Limits the denominator of all `Fraction` objects in this
    vector to some upper bound.

Arguments
- max_denominator: The largest allowed denominator.

Possible Errors
- ZeroDivisionError: If `max_denominator` is 0.

<!--This file has been automatically generated-->
