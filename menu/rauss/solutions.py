import numpy as np

class RaussCriteria:
    def __init__(self, coeffiecients: list):
        self.c: list = coeffiecients
        self.count: int = len(self.c)
        self.columns: int = math.ceil(self.count / 2)
        self.matrix = np.zeros(self.columns * 2 - self.count % 2, self.columns)

    def __set(self, dim: int, i: int, no: int) -> int:
        self.matrix[dim][no] = self.c[i]
        return no + 1

    def __first_rows(self):
        top: int = 1; bottom: int = 1

        for i in range(1, self.count):
            if i % 2 == 1:
                top = self.__set(1, i, top)
            else:
                bottom = self.__set(2, i, bottom)

    def __main_body(self, rows: int, matrix):
        for i in range(3, rows - 1):
            for j in range(1, self.columns - 1):
                basis: float = self.matrix[i - 1][1]

                left: float = basis * self.matrix[i - 2][j + 1]
                right: float = self.matrix[i - 2][1] * self.matrix[i - 1][j + 1]

                basis = 1 if basis == 0 else basis
                matrix[i][j] = left - right / basis

    def __define_poles(self):
        self.RHP: float = 0
        self.result = not any(self.matrix[:][1] <= 0)

        if self.result:
            signs: list = self.matrix[:][1] > 0
            end: int = len(signs)
            self.RHP = sum(__xor(signs[1:end - 1], signs[2:end]))

        self.LHP: float = (self.count - 1) - self.RHP

    @staticmethod
    def __xor(l1: list, l2: list) -> list:
        return [x ^ y for x, y in zip(l1, l2)]

    def study(self):
        self.result = all(self.c) == 0

        self.__first_rows()
        rows: int = len(self.matrix[1])

        self.__main_body(rows, self.matrix)

        matrix[rows][1] = self.matrix[rows - 2][2]
        self.__define_poles()
