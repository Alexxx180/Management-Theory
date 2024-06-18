from numpy import linspace
from common.commander.resources import Resources

def update(y: list, x: float, derives: list):
    for i in range(len(y)):
        y[i] = derives[i](x)

def tangent(precision: float, research):
    x = list(research.roots)

    y = [0.0, 0.0]
    update(y, x[0], research.derives)

    result = []

    a = lambda y, m: abs(y) / m

    while (n := a(y[0], x[1])) > precision:
        result.append([x[0], y[0], y[1], n])
        x[0] -= y[0] / y[1]
        update(y, x[0], research.derives)

    update(y, x[0], research.derives)

    row = [x[0], y[0], y[1], 0]
    if y[0] != 0:
        row[3] = a(y[0], x[1])

    result.append(row)
    return result

def draw(row: list, name: str, length: int):
    orders = []
    colors: tuple = ('green', 'blue', 'red')
    i: int = 0

    for index, value in enumerate(row):
        x = float(value[0])
        y = float(value[1])
        z = float(value[2])
        half: float = length / 2

        points = linspace(x - half, x + half, length)
        tangent = z * (points - x) + y

        i = (i + 1) % len(colors)

        caption: str = Resources.Texts[name]['Name'].format(index)
        order: tuple = (points, tangent, caption, x, y, colors[i])

        orders.append(order)

    return orders
