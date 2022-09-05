import random
import time
from fractions import Fraction

from momlib import Matrix, Vector

random.seed(time.time_ns())


def maybe(chance: float = 0.5) -> bool:
    return random.random() < chance


def rand_num() -> Fraction:
    return Fraction(random.randint(1, 1000), random.randint(1, 1000)) * (
        1 if maybe() else -1
    )


def rand_mat(rows: int, cols: int) -> Matrix:
    return Matrix(((rand_num() for _ in range(cols)) for _ in range(rows)))


def rand_vec(length: int) -> Vector:
    return Vector((rand_num() for _ in range(length)))


def rand_index(start: int = 1, end: int = 10) -> int:
    return random.randint(start, end)
