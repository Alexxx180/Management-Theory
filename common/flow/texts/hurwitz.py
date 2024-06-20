from common.drawing.table.table import Table
from common.handlers.interaction import pause
from common.handlers.printer import Printer
from common.commander.resources import Resources

class Text:
    def __init__(self, name: str):
        self.fields: dict = Resources.Fields[name]
        self.p = Printer(name).act(print)

    def formula(self, formula, initial):
        self.p.keys('Formula').args(formula).print()
        self.p.keys('Research').args(initial).print()

    def not_stable(self):
        self.p.keys('Not Stable').args().print()

    def stable(self, result):
        self.p.keys('Stable').args(result).print()

    def queue(self, orders: list):
        for order in orders:
            Table().rows(order[0]).show()
            self.p.keys('Determinant').args(order[1]).print()
            if len(order) > 2: 
                self.p.keys(order[2]).args().print()
        return self

    def pause(self, text: str = ''):
        pause(text)
