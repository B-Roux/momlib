# type: ignore - here be dragons
#
# curses is kind of a nightmare to work with unless you build your
# entire app using it. Since I don't want to do that, this is where all
# of the messy code will happen.
#
# This module file should expose only the `get_matrix_cli()` function.
# It must provide the user with a curses/CLI interface for defining a
# matrix, return the matrix when done, and handle opening/closing the
# curses window.
#
# This file is a top priority for refactoring.
# Last updated: 2022-05-23

import curses
import re
from fractions import Fraction
from typing import Tuple, List

from momlib.linalg.matrix import Matrix


class _StringCell(object):
    # Container that provides methods for handling the construction and
    # formatting of strings as part of a _StringMatrix.
    # This class should never be used outside of this file.

    def __init__(self, value: str):
        self._value = value
        self._len = len(value)

    def export(self, length: int):
        # Export the string centered in a length-width column
        assert len(self._value) <= length, "critical formatting error"
        len_b = (length - len(self)) // 2
        len_a = length - (len(self) + len_b)
        return (
            (" " * len_a)
            + (self._value if self._value != "" else "\u25AF")
            + (" " * len_b)
        )

    def raw(self):
        # Return the raw value (excluding any pretty formatting
        # characters, use for value processing)
        return self._value.strip(">_")

    def chval(self, newvalue: str):
        # change the stored value
        self._value = newvalue
        self._len = len(newvalue)

    def __len__(self):
        # length of the **RAW** value, but INCLUDING pretty formatting
        # characters.
        return max(self._len, 1)


class _StringMatrix(object):
    # Container that provides methods for handling the construction and
    # formatting of a matrix of strings.
    # This class should never be used outside of this file.

    def __init__(self):
        self._value = [[_StringCell("")]]
        self._rows = 1
        self._cols = 1
        self._req_space = (None, None)

    def add_blank_row(self):
        # Add a blank row of string cells
        self._value.append([_StringCell("") for _ in range(self._cols)])
        self._rows += 1

    def add_blank_col(self):
        # Add a blank column of string cells
        for row in self._value:
            row.append(_StringCell(""))
        self._cols += 1

    def mod_cell(self, coord: Tuple[int, int], value: str):
        # Modify a cell value, create the cell (and necessary rows/cols)
        # as needed.
        while coord[0] >= self._rows:
            self.add_blank_row()
        while coord[1] >= self._cols:
            self.add_blank_col()
        self._value[coord[0]][coord[1]].chval(value)

    def get_cell(self, coord: Tuple[int, int]):
        # Get a cell value, create the cell (and necessary rows/cols)
        # as needed.
        while coord[0] >= self._rows:
            self.add_blank_row()
        while coord[1] >= self._cols:
            self.add_blank_col()
        return self._value[coord[0]][coord[1]].raw()

    def trim(self, coord: Tuple[int, int]):
        # Soft-delete (ignore) the rows and columns greater than the
        # trim coords. Return the closest valid indices.
        coord = (max(coord[0], 1), max(coord[1], 1))
        self._rows = coord[0]
        self._cols = coord[1]
        return coord[0] - 1, coord[1] - 1

    def export_2d_arr(self) -> List[List[Fraction]]:
        # Export the non-ignored rows and columns for processing
        return [
            [
                Fraction(self._value[row][col].raw())
                for col in range(self._cols)
            ]
            for row in range(self._rows)
        ]

    def __str__(self):
        # Convert to a string representation
        col_lens = [
            max([len(self._value[i][j]) for i in range(self._rows)])
            for j in range(self._cols)
        ]
        dat_str = "\u2502\n\u2502".join(
            [
                "".join(
                    [
                        f" {self._value[row][col].export(col_lens[col])} "
                        for col in range(self._cols)
                    ]
                )
                for row in range(self._rows)
            ]
        )
        line_len = sum(col_lens) + (2 * len(col_lens))
        size_statement = f"(size: {self._rows}\u00D7{self._cols})"

        return (
            f'\u250C{" "*line_len}\u2510\n'
            f"\u2502{dat_str}\u2502 {size_statement}\n"
            f'\u2514{" "*line_len}\u2518'
        )

    def req_space(self):
        return self._req_space


class __StaticMatrixHolder(object):
    # static container for transferring the matrix from a curses window
    # to the value-returning function.
    # **Handle with care!** This can cause many issues, but it is the
    # cleanest way of dealing with this problem.
    # This class should never be used outside of this file.

    @classmethod
    def set_static_value(cls, value: Matrix | None) -> None:
        cls._matrix = value

    @classmethod
    def get_static_value(cls) -> Matrix:
        if isinstance(cls._matrix, Matrix):
            return cls._matrix
        else:
            raise TypeError("matrix not set")

    @classmethod
    def delete_value(cls):
        cls._matrix = None


def _main(stdscr):
    # prompt and get a matrix from the user.
    # This function WILL NOT RETURN ANYTHING, but it will fill the
    # __StaticMatrixHolder object with the matrix.

    curses.curs_set(0)  # make the cursor invisible
    current_row = 0
    current_col = 0
    mat = _StringMatrix()

    allowed_pattern = re.compile(r"-?[0-9]+((/|\.)[0-9]+)?")

    def validate_allowed(raw: str) -> str:
        vid = re.search(allowed_pattern, raw)
        if vid is None:
            return ""
        else:
            return raw[vid.start() : vid.end()]

    trim_confirmation = (None, None)
    first_iter = True

    message = ""

    while True:

        key = stdscr.getch() if not first_iter else 0
        character = chr(key) if not first_iter else ""
        bs = False
        text_input = ""

        if first_iter:
            first_iter = False
            message = "Editor Opened"

        elif key == curses.KEY_UP:
            mat.mod_cell(
                (current_row, current_col),
                validate_allowed(mat.get_cell((current_row, current_col))),
            )  # ensure the previous cell is correctly formatted
            trim_confirmation = (None, None)  # reset trim
            if current_row > 0:
                current_row -= 1
                message = "\u2191"

        elif key == curses.KEY_DOWN:
            mat.mod_cell(
                (current_row, current_col),
                validate_allowed(mat.get_cell((current_row, current_col))),
            )  # ensure the previous cell is correctly formatted
            trim_confirmation = (None, None)  # reset trim
            current_row += 1
            message = "\u2193"

        elif key == curses.KEY_LEFT:
            mat.mod_cell(
                (current_row, current_col),
                validate_allowed(mat.get_cell((current_row, current_col))),
            )  # ensure the previous cell is correctly formatted
            trim_confirmation = (None, None)  # reset trim
            if current_col > 0:
                current_col -= 1
                message = "\u2190"

        elif key == curses.KEY_RIGHT:
            mat.mod_cell(
                (current_row, current_col),
                validate_allowed(mat.get_cell((current_row, current_col))),
            )  # ensure the previous cell is correctly formatted
            trim_confirmation = (None, None)  # reset trim
            current_col += 1
            message = "\u2192"

        elif character == "\b":  # backspace
            bs = True
            message = "\u232B"

        elif key == 330:
            if trim_confirmation == (current_row, current_col):
                current_row, current_col = mat.trim(
                    (current_row + 1, current_col + 1)
                )
                trim_confirmation = (None, None)
                message = "Matrix Trimmed"
            else:
                trim_confirmation = (current_row, current_col)
                message = "Trim Matrix? (delete to confirm)"

        elif character == "\n":
            trim_confirmation = (None, None)  # reset trim
            try:
                __StaticMatrixHolder.set_static_value(
                    Matrix(mat.export_2d_arr())
                )
                del stdscr
                return
            except Exception as e:
                __StaticMatrixHolder.set_static_value(None)
                message = "Syntax Error: " + str(e)

        elif key == curses.KEY_RESIZE:  # avoids garbage input
            trim_confirmation = (None, None)  # reset trim
            message = "Terminal Resized"

        else:  # handle alphanumeric input
            trim_confirmation = (None, None)  # reset trim
            text_input += character
            message = f"Key Pressed: ({key})"

        cell_text = (
            mat.get_cell((current_row, current_col)) + text_input
            if not bs
            else ""
        )
        mat.mod_cell((current_row, current_col), f">{cell_text}_")

        stdscr.clear()
        try:
            stdscr.addstr(0, 0, f"Matrix Creator [{message}]")
            stdscr.addstr(2, 0, str(mat))
        except Exception as e:
            stdscr.addstr(
                1,
                0,
                "Too Large to Print: " "Trim the matrix or resize the window",
            )
        stdscr.refresh()

        mat.mod_cell((current_row, current_col), cell_text)


def get_matrix_cli() -> Matrix:
    # side-effect: sets the __StaticMatrixHolder class
    curses.wrapper(_main)

    # Read and reset the side-effected __StaticMatrixHolder class
    mat = __StaticMatrixHolder.get_static_value()
    __StaticMatrixHolder.delete_value()

    # Return, it's over :)
    return mat
