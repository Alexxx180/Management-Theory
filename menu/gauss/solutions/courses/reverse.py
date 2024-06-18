from numpy import zeros, dot
from common.drawing.table.table import Table

def step(text, x: list, i: int, a: list, b: list):
    start: int = i + 1

    scalar = dot(a[i, start:], x[start:])
    x[i] = (b[i] - scalar) / a[i, i]

    text.reverse_step(i, x[i])

def reverse(text, n: int, a, b: list):
    text.reverse_course()
    x = zeros(n)

    start: int = a.shape[0] - 1

    for i in range(start, -1, -1):
        step(text, x, i, a, b)
