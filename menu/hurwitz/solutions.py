import numpy as np
import sys

class HurwitzResearch:
    def __init__(self, coefficients: list):
        self.c: list = coefficients
        self.count: int = len(self.c)
        self.matrix: list = create()

    @staticmethod
    def __form(d: float, k: float) -> float:
        return 2 * d + 1 - k

    @staticmethod
    def __column(k: float, count: int) -> list:
        column: list = []
        for d in range(0, count, 2):
            f = __form(d, k)
            if f < 0:
                column.append(0)
            else:
                try:
                    column.append(self.c[f])
                except IndexError:
                    column.append(0)
        return column

    @staticmethod
    def create() -> list:
        count: int = self.count - 1
        matrix: list = [__column(k, count) for k in range(0, count)]
        return np.array(matrix)

    @staticmethod
    def __slice(self, no: int, shape: int):
        return np.array(list(range(no)) + list(range(no + 1, shape)))

    def __remove_cross(self) -> list:
        s = self.matrix.shape
        row, column = s
        return self.matrix[__slice(row, s[0]), __slice(column, s[1])]

    def __answer(self, d: float):
        print(self.matrix)
        text.keys("Determinant").args(d)
        if d == 0: text.keys("Margin")

    def __determinator(self) -> float:
        return np.linalg.det(self.matrix)

    def study(self) -> bool:
        d: float = __determinator()
        self.__answer(d)

        if d < 0:
            return False
        else:
            text.keys("Greater")

        for _ in range(0, self.count - 2):
            self.matrix = self.__remove_cross()
            d = __determinator()
            self.__answer(d)

            if d < 0: return False

        return True
