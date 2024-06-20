from common.commander.switch import View
from common.flow.texts.hurwitz import Text
from common.handlers.input.formula import from_formula
from menu.hurwitz.solutions import HurwitzCriteria

"""This program takes a linear system's characteristic equation (its coefficients) and checks the system's stability against the Hurwitz stability criterion."""

def HurwitzMethod(name: str, formula: str):
    args: list = from_formula(formula)

    criteria = HurwitzCriteria(args)
    text = Text(name)
    text.formula(formula, criteria)
    criteria.study()

    if View('Table', name):
        text.queue(criteria.orders)

    if criteria.d >= 0:
        text.stable(criteria)
    else:
        text.not_stable()

    text.pause()
