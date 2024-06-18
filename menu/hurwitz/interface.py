from common.flow.texts.tangent import Text
from common.commander.switch import View
from common.flow.canvas.tangent import canvas_from
from menu.tangent.solutions.functions import tangent, draw
from menu.tangent.solutions.research import Research

"""This program takes a linear system's characteristic equation (its coefficients) and checks the system's stability against the Hurwitz stability criterion."""

def HurwitzMethod(name: str, formula: str):
    args: list = from_formula(formula)

    research = Research(name)
    research.start(args)

    text = Text(name)
    text.formula(formula)

    matrix = create_hurwitz_matrix(coefficients)
    text.key("Hurwitz")

    research.study(newmatrix, coefficients)
    text.print(research.result)

    newmatrix = matrix
    research.study(newmatrix, coefficients)
    text.print(research.result)

    if View('Table', name): text.result(research.newmatrix)

    text.pause()