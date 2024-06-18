from sympy.abc import x
from common.commander.switch import View
from common.commander.resources import Resources
from common.calculus.trigonometry import formulate, invokation
from menu.division.solutions import SegmentDivision
from common.flow.canvas.division import canvas_from
from common.flow.texts.division import Text

def SegmentDivisionMethod(name: str, args: tuple):
    formula = formulate(Resources.Formula[name], 0, x)
    derive = invokation(formula, x)

    canvas = canvas_from(name, derive, args)

    division = SegmentDivision(args, derive)

    text = Text(name)
    text.research(formula, division)

    division.study()

    if len(division.roots) == 0:
        text.no_roots()
    else:
        if View('Table', name):
            text.source(division.roots)
        text.result(division)

    if View('Plots', name):
        canvas.show(division.orders)
    text.pause()
