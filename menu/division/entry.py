from common.commander.switch import are_defaults
from common.commander.resources import Resources
from menu.division.interface import SegmentDivisionMethod

def DivisionEntry():
    name = 'Division'

    if are_defaults():
        args = Resources.Defaults[name]
    else:
        args = Resources.Input[name]()

    SegmentDivisionMethod(name, args)
