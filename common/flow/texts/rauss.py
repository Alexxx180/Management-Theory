from common.drawing.table.table import Table
from common.handlers.printer import Printer
from common.handlers.interaction import pause
from common.commander.resources import Resources

class Text:
    def __init__(self, name: str):
        self.fields: dict = Resources.Fields[name]
        self.p = Printer(name).act(print)

    def research(self, formula, initial):
        if 'p' in formula:
            self.p.keys('Formula').args(formula).print()
        self.p.keys('Research').args(initial).print()

    def not_stable(self):
        self.p.keys('Not Stable').args().print()

    def stable(self, result):
        self.p.keys('Stable').args(result).print()

    def source(self, matrix):
        Table().rows(matrix).show()
        return self

    def result(self, *args):
        self.p.keys('Result').args(*args).print()

    def pause(self): pause()
