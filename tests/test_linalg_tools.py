from typing import List
import unittest
from fractions import Fraction

from tests.helpers import rand_mat, rand_vec, rand_index

import momlib._linalg as _linalg
from momlib import (
    Matrix,
    Vector,
    LinearDependenceError,
    RectangularMatrixError,
    DimensionMismatchError,
)


class TestLinalgTools(unittest.TestCase):
    def test_angle(self):
        with self.assertRaises(DimensionMismatchError):
            _linalg.angle(Vector([56, 94]), Vector([62, 72, 56]))
        vec1 = Vector([56, 94])
        vec2 = Vector([63, 65])
        self.assertAlmostEqual(
            _linalg.angle(vec1, vec2), 0.232489720476199743033978670459828
        )
        vec3 = Vector([62, 72, 56])
        vec4 = Vector([48, 93, 61])
        self.assertAlmostEqual(
            _linalg.angle(vec3, vec4), 0.202199804245784539599222286887168
        )
        vec5 = Vector([25, 84, 45, 85])
        vec6 = Vector([22, 74, 86, 85])
        self.assertAlmostEqual(
            _linalg.angle(vec5, vec6), 0.294931109036742288496989100615401
        )
        vec7 = Vector([1, 0])
        vec8 = Vector([0, 1])
        self.assertAlmostEqual(
            _linalg.angle(vec7, vec8), 1.570796326794896619231321691639751
        )
        vec7 = Vector([1, 0])
        vec8 = Vector([1, 0])
        self.assertAlmostEqual(_linalg.angle(vec7, vec8), 0)

    def test_cross(self):
        vec1 = Vector([1, 2, 3])
        self.assertEqual(_linalg.cross(vec1, vec1 * 2), Vector([0, 0, 0]))
        for _ in range(10):
            vec1 = rand_vec(3)
            vec1l = vec1.elements
            vec1l[1] += 1
            vec2 = Vector(vec1l)
            vec3 = _linalg.cross(vec1, vec2)
            self.assertEqual(vec1 @ vec3, 0)
            self.assertEqual(vec2 @ vec3, 0)
        for i in range(2, 10):
            vecs: List[Vector] = []
            for _ in range(i - 1):
                vecs.append(rand_vec(i))
            cross = _linalg.cross(*vecs)
            for item in vecs:
                self.assertEqual(cross @ item, 0)
        vec4 = Vector([-3, 0, -2])
        vec5 = Vector([5, -1, 2])
        vec6 = Vector([-2, -4, 3])
        self.assertEqual(_linalg.cross(vec4, vec5), vec6)

    def test_determinant_laplace(self):
        for i in range(1, 5):
            mat1 = _linalg.identity(i)
            self.assertEqual(_linalg.determinant(mat1), Fraction(1))
        for i in range(1, 5):
            mat1 = rand_mat(i, i)
            self.assertEqual(
                _linalg.determinant(_linalg.transpose(mat1)),
                _linalg.determinant(mat1),
            )

        def laplace_determinant(matrix: Matrix) -> Fraction:
            if matrix.shape == (1, 1):
                return matrix[0, 0]
            elif matrix.shape == (2, 2):
                return (matrix[0, 0] * matrix[1, 1]) - (
                    matrix[1, 0] * matrix[0, 1]
                )
            else:
                return sum(
                    (
                        laplace_determinant(tup[0]) * tup[1]
                        for tup in _linalg.laplace_expansion(matrix)
                    ),
                    start=Fraction(0),
                )

        for i in range(10):
            for dim in range(1, 7):
                mat1 = rand_mat(dim, dim)
                self.assertEqual(
                    _linalg.determinant(mat1), laplace_determinant(mat1)
                )
        with self.assertRaises(RectangularMatrixError):
            _linalg.determinant(rand_mat(2, 3))
        with self.assertRaises(RectangularMatrixError):
            _linalg.determinant(rand_mat(3, 2))

        mat2 = Matrix([[3, 0, 1], [1, 2, 5], [-1, 4, 2]])
        self.assertEqual(_linalg.determinant(mat2), -42)

    def test_distance(self):
        vec1 = Vector([0, 3])
        vec2 = Vector([0, 5])
        self.assertAlmostEqual(_linalg.distance(vec1, vec2), 2.0)
        vec3 = Vector([3, 5, 2, 8])
        vec4 = Vector([6, 3, 2, 5])
        self.assertAlmostEqual(
            _linalg.distance(vec3, vec4), 4.690415759823429554565630113544466
        )
        with self.assertRaises(DimensionMismatchError):
            _linalg.distance(rand_vec(2), rand_vec(3))
        with self.assertRaises(DimensionMismatchError):
            _linalg.distance(rand_vec(3), rand_vec(2))

    def test_homogenous(self):
        mat1 = _linalg.homogenous((5, 5), 1)
        for i in range(5):
            for j in range(5):
                self.assertEqual(mat1[i, j], Fraction(1))
        mat2 = _linalg.homogenous((2, 6), 1)
        for i in range(2):
            for j in range(6):
                self.assertEqual(mat2[i, j], Fraction(1))
        mat3 = _linalg.homogenous((3, 3), 5)
        mat4 = Matrix([[5, 5, 5], [5, 5, 5], [5, 5, 5]])
        self.assertEqual(mat3, mat4)

        vec1 = _linalg.homogenous(5, 1)
        for i in range(5):
            self.assertEqual(vec1[i], 1)
        vec2 = _linalg.homogenous(3, 5)
        vec3 = Vector([5, 5, 5])
        self.assertEqual(vec2, vec3)

    def test_identity(self):
        mat1 = _linalg.identity(5)
        for i in range(5):
            for j in range(5):
                self.assertEqual(mat1[i, j], 1 if i == j else 0)
        mat2 = _linalg.identity(3)
        mat3 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertEqual(mat2, mat3)

    def test_inverse(self):
        for _ in range(10):
            for i in range(1, 7):
                mat1 = rand_mat(i, i)
                try:
                    mat1_inv = _linalg.inverse(mat1)
                    self.assertEqual(mat1 @ mat1_inv, _linalg.identity(i))
                except (LinearDependenceError):
                    pass  # shouldn't happen often, just skip if it does
        with self.assertRaises(LinearDependenceError):
            vec1 = Vector([1, 2, 3])
            mat2 = _linalg.matcat(vec1, vec1 * 2, vec1 * 3)
            _linalg.inverse(mat2)
        mat3 = Matrix([[-1, 2, 3], [4, -5, 6], [7, 8, -9]])
        mat4 = Matrix(
            [
                [Fraction(-1, 120), Fraction(7, 60), Fraction(3, 40)],
                [Fraction(13, 60), Fraction(-1, 30), Fraction(1, 20)],
                [Fraction(67, 360), Fraction(11, 180), Fraction(-1, 120)],
            ]
        )
        self.assertEqual(_linalg.inverse(mat3), mat4)

    def test_join_separate_vectors(self):
        vec1 = Vector([1, 2, 3])
        vec2 = Vector([4, 5, 6])
        vec3 = Vector([7, 8, 9])
        vec4 = Vector([1, 2])
        mat1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        mat2 = Matrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        self.assertEqual(
            mat1, _linalg.matcat(vec1, vec2, vec3, column_wise=False)
        )
        self.assertEqual(
            mat2, _linalg.matcat(vec1, vec2, vec3, column_wise=True)
        )
        with self.assertRaises(DimensionMismatchError):
            _linalg.matcat(vec1, vec2, vec4)
        self.assertEqual(mat1, _linalg.matcat(*_linalg.get_vectors(mat1)))
        self.assertEqual(
            mat1,
            _linalg.matcat(
                *_linalg.get_vectors(mat1, column_wise=False),
                column_wise=False
            ),
        )
        self.assertEqual(
            mat1,
            _linalg.matcat(
                *_linalg.get_vectors(mat1, column_wise=True), column_wise=True
            ),
        )
        self.assertEqual(
            mat2,
            _linalg.matcat(
                *_linalg.get_vectors(mat1, column_wise=False), column_wise=True
            ),
        )

    def test_limit_denominator(self):
        max_denom = rand_index(20, 50)

        for row in _linalg.limit_denominator(rand_mat(5, 5), max_denom):
            for item in row:
                self.assertLessEqual(item, max_denom)

        for item in _linalg.limit_denominator(rand_vec(5), max_denom):
            self.assertLessEqual(item, max_denom)

    def test_normalize_magnitude(self):
        for _ in range(10):
            vec = rand_vec(5)
            norm = _linalg.normalize(vec)
            self.assertAlmostEqual(_linalg.magnitude(norm), 1.0)

    def test_orthogonalize(self):
        orthos1 = _linalg.orthogonalize(
            Vector([1, 1, 1]), Vector([1, 1, 2]), Vector([2, 1, 1])
        )
        for i in range(3):
            for j in range(3):
                if i == j:
                    pass
                else:
                    self.assertEqual((orthos1[i] @ orthos1[j]), 0)

    def test_rank_row_reduce(self):
        mat1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(
            _linalg.row_reduce(mat1),
            Matrix([[1, 0, -1], [0, 1, 2], [0, 0, 0]]),
        )
        for _ in range(10):
            size = (rand_index(), rand_index())
            mat2 = _linalg.row_reduce(rand_mat(*size), rref=True)
            pivot = 0
            for row in range(size[0]):
                if pivot >= size[1]:
                    for col in range(size[1]):
                        self.assertEqual(mat2[row, col], 0)
                else:
                    for col in range(0, pivot):
                        self.assertEqual(mat2[row, col], 0)
                    while pivot < size[1] and mat2[row, pivot] == 0:
                        pivot += 1
                    if pivot < size[1] - 1:
                        self.assertEqual(mat2[row, pivot], 1)

    def test_transpose(self):
        for i in range(1, 10):
            mat = rand_mat(i, 10 - i)
            tps = _linalg.transpose(mat)
            for row in range(i):
                for col in range(10 - i):
                    self.assertEqual(mat[row, col], tps[col, row])


if __name__ == "__main__":
    unittest.main()
