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
        no: int = i % 2
        self.matrix[no][edges[no]] = self.c[i]
        edges[no] += 1

    def __first_rows(self):
        edges: list = [0, 0]
        for i in range(0, self.count):
            self.__set(edges, i)

    def __formula(self, row1: list, row2: list, j: int) -> float:
        div: float = 1 if row1[0] == 0 else row1[0]
        return row2[j] - row2[0] / div * row1[j]

    def __calculate(self, i: int):
        for j in range(0, self.columns - 1):
            row2: list = self.matrix[i - 2]
            row1: list = self.matrix[i - 1]
            self.matrix[i][j] = self.__formula(row1, row2, j + 1)

    def __main_body(self, rows: int):
        for i in range(2, rows):
            self.__calculate(i)

    def __xor(self, l1: list, l2: list) -> list:
        return [x ^ y for x, y in zip(l1, l2)]

    def __define_poles(self):
        self.RHP: float = 0
        self.result = any(self.matrix[:][0] <= 0)

        if self.result:
            signs: list = self.matrix[:][0] > 0
            end: int = len(signs)
            self.RHP = sum(self.__xor(signs[0:end - 1], signs[1:end]))

        self.result = not self.result
        self.LHP: float = (self.count - 1) - self.RHP

    def study(self):
        #self.result = all(self.c) == 0
        self.__first_rows()
        self.__main_body(len(self.matrix))
        self.__define_poles()
