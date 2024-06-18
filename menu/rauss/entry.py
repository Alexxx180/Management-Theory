from common.commander.switch import are_defaults
from common.commander.resources import Resources
from menu.division.interface import RaussCriteriaMethod

def DivisionEntry(key):
    name = 'Rauss'

    if are_defaults():
        formula = Resources.Formula[name][key]
    else:
        formula = Resources.Input[name]()

    RaussCriteriaMethod(name, formula)
