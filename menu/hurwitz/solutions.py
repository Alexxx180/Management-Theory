import numpy as np
import sys

class HurwitzCriteria:
    def __init__(self, coefficients: list):
        self.c: list = coefficients
        self.count: int = len(self.c) - 1
        self.matrix: list = self.create()
        print(self.matrix)

    @staticmethod
    def __form(d: float, k: float) -> float:
        return 2 * d + 1 - k

    def __column(self, k: float) -> list:
        column: list = []
        for d in range(0, self.count, 2):
            f = HurwitzCriteria.__form(d, k)
            column.append(self.c[f] if f > 0 and f < len(self.c) else 0)
        return column

    def create(self) -> list:
        matrix: list = [self.__column(k, self.count) for k in range(0, self.count)]
        return np.array(matrix)

    @staticmethod
    def __slice(no: int, shape: int):
        return np.array(list(range(no)) + list(range(no + 1, shape)))

    def __cross_cut(self) -> list:
        s = self.matrix.shape
        row, column = s
        return self.matrix[
            HurwitzCriteria.__slice(row - 1, s[0])[:,np.newaxis],
            HurwitzCriteria.__slice(column - 1, s[1])
        ]

    def __answer(self, d: float):
        text.keys("Determinant").args(d)
        if d == 0: text.keys("Margin")

    def __check(self) -> bool:
        determinator: float = np.linalg.det(self.matrix)
        self.__answer(determinator)
        self.result: bool = not determinator < 0
        return not self.result

    def study(self):
        if self.__check(): return
        text.keys("Greater")

        for _ in range(0, self.count - 1):
            self.matrix = self.__cross_cut()
            if self.__check(): return
