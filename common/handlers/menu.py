from common.handlers.interaction import ask
from menu.division.entry import DivisionEntry
from menu.tangent.entry import TangentEntry
from menu.gauss.entry import GaussEntry
from menu.simpson.entry import SimpsonFormulaEntry
from menu.runge.entry import RungeKuttaEntry

invoke: dict = {
    'division': DivisionEntry,
    'tangent': TangentEntry,
    'gauss': GaussEntry,
    'simpson': SimpsonFormulaEntry,
    'runge': RungeKuttaEntry
}

def select(query: str, choices: dict, options: dict):
    answers = ask(options[query])
    for key, value in choices.items():
        if answers[query] == key:
            invoke[query](value)
