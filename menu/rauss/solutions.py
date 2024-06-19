import numpy as np
from math import ceil

class RaussCriteria:
    def __init__(self, coeffiecients: list):
        self.c: list = coeffiecients
        self.count: int = len(self.c)
        self.columns: int = ceil(self.count / 2)
        x: int = self.columns * 2 - self.count % 2
        self.matrix = np.zeros((x, self.columns))

    def __set(self, edges: list, i: int) -> int:
        no: int = 1 - i % 2
        self.matrix[no][edges[no]] = self.c[i]
        edges[no] += 1

    def __first_rows(self):
        edges: list = [0, 0]
        for i in range(1, self.count):
            self.__set(edges, i)

    def __formula(self, row1: list, row2: list, j: int, div: float):
        return row1[0] * row2[j] - row2[0] * row1[j] / div

    def __calculate(self, i: int):
        for j in range(2, self.columns):
            print(i - 2)
            print(self.matrix)
            row2: list = self.matrix[i - 2]
            row1: list = self.matrix[i - 1]
            div: float = 1 if row1[0] == 0 else row1[0]

            self.matrix[i][j - 1] = self.__formula(row1, row2, j, div)

    def __main_body(self, rows: int):
        for i in range(2, rows - 1):
            self.__calculate(i)

    def __xor(self, l1: list, l2: list) -> list:
        return [x ^ y for x, y in zip(l1, l2)]

    def __define_poles(self):
        self.RHP: float = 0
        self.result = not any(self.matrix[:][0] <= 0)

        if self.result:
            signs: list = self.matrix[:][0] > 0
            end: int = len(signs)
            self.RHP = sum(self.__xor(signs[0:end - 1], signs[1:end]))

        self.LHP: float = (self.count - 1) - self.RHP

    def study(self):
        self.result = all(self.c) == 0
        self.__first_rows()
        rows: int = len(self.matrix[0])
        self.__main_body(rows)
        self.matrix[rows][0] = self.matrix[rows - 2][1]
        self.__define_poles()
