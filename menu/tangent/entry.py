from common.commander.switch import are_defaults
from common.commander.resources import Resources
from menu.tangent.interface import TangentMethod

def TangentEntry(key):
    name = 'Tangent'

    if are_defaults():
        args = Resources.Defaults[name][key]
    else:
        args = Resources.Input[name]()

    TangentMethod(key, name, args)
