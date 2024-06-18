import numpy as np
from inquirer import prompt, Text
from menu.gauss.solutions.checks import is_single, is_varying
from menu.gauss.interface.errors import Errors

class InputLoop:
    def __init__(self, text):
        self.text = text
        self.empty = 'empty'
        self.vary = 'vary'
        self.errors = Errors((self.empty, 'invalid', self.vary))

    def __process(self, row) -> bool:
        try:
            self.row = [float(cell) for cell in row.split()]
            return False
        except ValueError:
            self.text.process()
            return True

    def __prompt(self, count: int):
        if count == 0:
            not_vary = lambda: False
        else:
            not_vary = lambda: is_varying(self, self.text, count)

        name = 'row'
        query = [Text(name, message=self.text.description())]
        row: str = prompt(query)[name]
        self.errors.compute((
            lambda: len(row) == 0,
            lambda: self.__process(row),
            not_vary
        ))

    def __validation(self):
        count: int = 0

        while not count == 0:
            self.__prompt(count)
            count = len(self.row)

        while not self.errors.at[self.empty]:
            self.__prompt(count)
            if not self.errors.total:
                self.columns.append(self.row)

    def perform(self):
        self.row: list = []
        self.columns: list = []
        self.__validation()

        if self.errors.at[self.vary] or len(self.columns) == 0:
            return False

        self.matrix = np.array(self.columns)
        shape = self.matrix.shape[0]

        return not is_single(shape, self.text)
