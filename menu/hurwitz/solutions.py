import numpy as np
import sys

class HurwitzCriteria:
    def __init__(self, coefficients: list):
        self.c: list = coefficients
        self.count: int = len(self.c) - 1
        self.matrix: list = self.create()
        self.orders: list = []

    @staticmethod
    def __form(d: float, k: float) -> float: return 2 * d + 1 - k

    def __column(self, k: float) -> list:
        column: list = []
        for d in range(0, self.count, 1):
            f = HurwitzCriteria.__form(d, k)
            column.append(self.c[f] if f >= 0 and f < len(self.c) else 0)
        return column

    def create(self) -> list:
        matrix: list = [self.__column(k) for k in range(0, self.count)]
        return np.array(matrix)

    def __slice(self, no: int, shape: int):
        return np.array(list(range(no)) + list(range(no + 1, shape)))

    def __cross_cut(self) -> list:
        s = self.matrix.shape
        row, column = s
        self.matrix = self.matrix[
            self.__slice(row - 1, s[0])[:, np.newaxis],
            self.__slice(column - 1, s[1])
        ]
        return self

    def __add(self, f1: callable, f2: callable):
        self.orders.append(f1() if self.d == 0 else f2())

    def __part(self) -> tuple:
        return (self.matrix, self.d)

    def __full(self, description: str) -> tuple:
        return (self.matrix, self.d, description)

    def __determinator(self) -> float:
        self.d: float = np.linalg.det(self.matrix)
        return self

    def study(self):
        if self.__determinator().d < 0: return

        edge = lambda: self.__full('Margin')
        self.__add(edge, lambda: self.__full('Greater'))

        i = self.count - 1
        while self.d >= 0 and i > 0:
            self.__cross_cut().__determinator()
            self.__add(edge, self.__part)
            i -= 1
