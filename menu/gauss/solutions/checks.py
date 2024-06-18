import numpy as np

def are_undefined(array, text):
    for row in array:
        if np.all(row[:-1] == 0) and row[-1] != 0:
            text.empty(row, 'None')
            return True
        if np.all(row == 0):
            text.empty(row, 'Many')
            return False

    index: int = array.shape[0] - 1
    row = array[index]

    no_zeros = not all(e == 0 for e in row[:-2])
    if no_zeros: text.zeros()
    return no_zeros

def is_suitable(shape):
    return shape[0] <= shape[1] - 1

def is_varying(self, text, count: int) -> bool:
    errors: bool = len(self.row) != count
    if errors: text.varying()
    return errors

def is_single(count: int, text) -> bool:
    if errors := count == 1: text.single()
    return errors
