import numpy as np

class RaussCriteria:
    def __init__(self, args: tuple):
        self.coeff = args

    def __first_rows(self, matrix):
        top: int = 1; bottom: int = 1

        for i in range(1, count):
            if i % 2 == 1:
                matrix[1][top] = coeff[i]
                top += 1
            else:
                matrix[2][bottom] = coeff[i]
                bottom += 1

    def __main_body(self, rows: int, matrix):
        for i in range(3, rows - 1):
            for j in range(1, columns - 1):
                common = matrix[i - 1][1]
                row = matrix[i - 2]

                left = common * row[j + 1]
                right = row[1] * matrix[i - 1][j + 1]

                divider = 1 if common == 0 else common
                matrix[i][j] = left - right / divider

    def __define_poles(self, matrix, count: int):
        self.RHP: int = 0
        if any(matrix[:][1] <= 0):
            signs = matrix[:][1] > 0
            end: int = len(signs)
            changes = __xor(signs[1:end - 1], signs[2:end])

            self.RHP = sum(changes)
            self.result = False
        else:
            self.result = True

        self.LHP: int = (count - 1) - self.RHP

    @staticmethod
    def __xor(l1: list, l2: list) -> list:
        return [x ^ y for x, y in zip(l1, l2)]

    def study(self):
        self.result = all(self.coeff) == 0
        count: int = len(self.coeff)
        columns: int = math.ceil(len / 2)

        matrix = np.zeros(columns * 2 - count % 2, columns)
        self.__first_rows(matrix)

        rows: int = len(matrix[1])
        self.__main_body(rows, matrix)

        matrix[rows][1] = matrix[rows - 2][2]
        self.__define_poles(matrix)
