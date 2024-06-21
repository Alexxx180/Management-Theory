from common.commander.switch import View
from common.flow.texts.rauss import Text
from common.handlers.input.formula import from_formula
from menu.rauss.solutions import RaussCriteria

def RaussCriteriaMethod(name: str, formula: str):
    args: list = from_formula(formula)

    criteria = RaussCriteria(args)
    text = Text(name)
    text.research(formula, criteria)
    criteria.study()

    if View('Table', name):
        text.source(criteria.matrix)

    if criteria.result:
        text.stable(criteria)
    else:
        text.not_stable()

    text.pause()
