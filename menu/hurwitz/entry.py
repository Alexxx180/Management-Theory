from common.commander.switch import are_defaults
from common.commander.resources import Resources
from menu.tangent.interface import HurwitzMethod

def HurwitzEntry():
    name = 'Hurwitz'

    if are_defaults():
        args = Resources.Formula[name]
    else:
        args = Resources.Input[name]()

    HurwitzMethod(key, name, args)
