import re
from common.commander.switch import View
from menu.criteria.solutions import RaussCriteria
from common.flow.texts.criteria import Text
from common.handlers.input.formula import from_formula

def RaussCriteriaMethod(name: str, formula: str):
    args: list = from_formula(formula)

    criteria = RaussCriteria(args)
    text = Text(name)
    text.research(formula, criteria)
    criteria.study()

    if criteria.result:
        if View('Table', name):
            text.source(criteria.matrix)
        text.stable(criteria)
    else:
        text.not_stable()
