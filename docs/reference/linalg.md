# Linear Algebra Tools

Provides an assortment of more advanced linear algebra tools to work
    with `Vector` and `Matrix` objects.

## Contents

- [cross](#cross)
- [determinant](#determinant)
- [distance](#distance)
- [get\_vectors](#get_vectors)
- [homogenous\_matrix](#homogenous_matrix)
- [homogenous\_vector](#homogenous_vector)
- [identity](#identity)
- [inverse](#inverse)
- [laplace\_expansion](#laplace_expansion)
- [magnitude](#magnitude)
- [matcat](#matcat)
- [matrix\_power](#matrix_power)
- [normalize](#normalize)
- [orthogonalize](#orthogonalize)
- [rank](#rank)
- [row\_reduce](#row_reduce)
- [transpose](#transpose)

---

# cross

```python
(*vectors: 'Vector') -> 'Vector'
```

Calculates a vector that is orthogonal to every given vector, in the
    case of exactly two 3-dimensional inputs, this is the cross
    product.

Arguments
- *vectors: The collection of vectors to cross (the number of
    vectors) given must be one less than the length of each vector.

Possible Errors
- ValueError: If the vectors given for `vectors` are not all the
    same length \_n\_, or if not exactly \_n\_-1 vectors were given.

---

# determinant

```python
(matrix: 'Matrix') -> 'Fraction'
```

Calculates the determinant of a matrix, which represents the scaling
    factor a matrix would apply when acting as a linear
    transformation.

Arguments
- matrix: The matrix for which the determinant is to be calculated.

Possible Errors
- RectangularMatrixError: If `matrix` is not a square matrix.

---

# distance

```python
(point_a: 'Vector', point_b: 'Vector') -> 'float'
```

Calculates the straight-line distance between two \_n\_-dimensional
    points given by vectors.

Arguments
- point\_a: The "starting" point.
- point\_b: The "ending" point.

Possible Errors
- DimensionMismatchError: If `point\_a` and `point\_b` do not have the
    same length.

Notes
- May introduce floating point errors.

---

# get\_vectors

```python
(matrix: 'Matrix', column_wise: 'bool' = True) -> 'Iterable[Vector]'
```

Lazily gets each row or column from a matrix as a vector.

Arguments
- matrix: The matrix to separate into vectors.
- column\_wise: Whether to interpret the given matrix as a collection
    of columns (when true), or a list of rows (when false).
    Optional, defaults to true.

---

# homogenous\_matrix

```python
(shape: 'tuple[int, int] | int', value: 'float | Fraction' = 0) -> 'Matrix'
```

Matrix constructor that creates a matrix of a given shape which has
    all elements equal to one another.

Arguments
- shape: The row-column shape of the desired matrix. If this is an
    integer, a square matrix with both sides of the specified length
    will be returned.
- value: The value with which to fill the matrix.
    Optional, defaults to 0.

---

# homogenous\_vector

```python
(length: 'int', value: 'float | Fraction' = 0) -> 'Vector'
```

Vector constructor that creates a vector of a given length which has
    all elements equal to one another.

Arguments
- length: The length of the desired vector.
- value: The value with which to fill the vector.
    Optional, defaults to 0.

---

# identity

```python
(side_length: 'int') -> 'Matrix'
```

Creates and returns a square identity matrix.

Arguments
- side\_length: The side-length of the desired matrix.

Possible Errors
- ValueError: If `side\_length` is 0 (or less).

---

# inverse

```python
(matrix: 'Matrix') -> 'Matrix'
```

Inverts a matrix with respect to matrix multiplication.

Arguments
- matrix: The matrix to invert.

Possible Errors
- RectangularMatrixError: If `matrix` is not a square matrix.
- LinearDependenceError: If `matrix` is non-invertible.

---

# laplace\_expansion

```python
(matrix: 'Matrix') -> 'Iterable[tuple[Matrix, Fraction]]'
```

Lazily yields the cofactor expansion of a matrix along its first row
    as a matrix-coefficient tuple.

Arguments
- matrix: The matrix to expand.

Possible Errors
- RectangularMatrixError: If `matrix` is not a square matrix.

---

# magnitude

```python
(vector: 'Vector') -> 'float'
```

Calculates the magnitude (length) of a given vector.

Arguments
- vector: The vector for which the magnitude must be calculated.

Notes
- May introduce floating point errors.

---

# matcat

```python
(*vectors: 'Vector', column_wise: 'bool' = True) -> 'Matrix'
```

Concatenates \_m\_ vectors of dimension \_n\_ into either an \_m\_ by \_n\_
    matrix, or an \_n\_ by \_m\_ matrix.

Arguments
- *vectors: The vectors to join.
- column\_wise: Whether to interpret the given vectors as columns
    (when true), or as rows (when false) of the desired matrix.
    Optional, defaults to true.

Possible Errors
- ValueError: If no vectors were given.
- DimensionMismatchError: If not all of the given vectors have the
    same length.

---

# matrix\_power

```python
(matrix: 'Matrix', power: 'int') -> 'Matrix'
```

Calculates the given integer power of a matrix by repeated matrix
    multiplication.

Arguments
- matrix: The matrix to raise to the given power.
- power: The power to raise the given matrix to.

Possible Errors
- RectangularMatrixError: If `matrix` is not a square matrix.

---

# normalize

```python
(vector: 'Vector') -> 'Vector'
```

Calculates an approximately normal vector.

Arguments
- vector: The vector to normalize.

Possible Errors
- ZeroDivisionError: If the magnitude of the given vector is 0.

Notes
- An exact normal cannot be calculated since normalization involves
    scaling by a possibly irrational factor. This may introduce
    floating point errors.

---

# orthogonalize

```python
(*vectors: 'Vector') -> 'list[Vector]'
```

Using the Gram-Schmidt process, creates an orthogonal basis from a
    set of vectors.

Arguments
- *vectors: The set of vectors to use as a non-orthogonal basis.

Possible Errors
- ValueError: If not all given vectors have the same length, or
    if not exactly *n* vectors are given, where *n* represents the
    length of each vector.
- LinearDependenceError: If the given vectors cannot form a linearly
    independent basis.

Notes
- The returned vectors are not normalized, they must be manually
    normalized if an orthonormal basis is sought.

---

# rank

```python
(matrix: 'Matrix') -> 'int'
```

Calculates the rank of a given matrix.

Arguments
- matrix: The matrix the rank is to be calculated from.

---

# row\_reduce

```python
(matrix: 'Matrix', rref: 'bool' = True) -> 'Matrix'
```

Computes a row-echelon or reduced row-echelon form matrix by row
    reduction.

Arguments
- matrix: The matrix to row-reduce.
- rref: Whether to compute the reduced row-echelon form by
    Gauss-Jordan elimination, or compute a non-reduced row-echelon
    form by simple Gaussian elimination.
    Optional, defaults to true.

---

# transpose

```python
(matrix: 'Matrix') -> 'Matrix'
```

Calculate the transpose of a given matrix.

Arguments
- matrix: The matrix to transpose.

<!--this file has been automatically generated-->
