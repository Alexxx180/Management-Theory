import re
from common.commander.switch import View
from menu.criteria.solutions import RaussCriteria
from common.flow.texts.criteria import Text

def from_formula(formula: str) -> list:
    args: list = []; coeffs: list = []

    for p1 in formula.split('+'):
        p2 = p1.split('-')
        coeffs.add(p2[0].strip())
        for i in range(1, len(p1)):
            coeffs.add('-' + p2[i].strip())

    for text in coeffs:
        i: int = p.index('p')
        if i == -1:
            args.append(int(p))
        else:
            args.append(int(p[:i]))
    # (1, 8, 32, 80, 100) # ...split
    #"A": "p3 + 2p2 + 2p + 1",
    #"B": "p4 + p3 + 3p2 + 2p + 1"
    return args

def RaussCriteriaMethod(name: str, formula: str):
    args: list = from_formula(formula)

    criteria = RaussCriteria(args)
    text = Text(name)
    text.research(formula, criteria)
    criteria.study()

    if criteria.result:
        #if View('Table', name):
        #    text.source(criteria.matrix)
        text.keys("Stable")
        text.result(criteria)
    else:
        text.keys("Not Stable")
        text.no_roots()
