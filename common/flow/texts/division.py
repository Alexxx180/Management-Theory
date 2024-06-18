from common.drawing.table.table import Table
from common.handlers.printer import Printer
from common.handlers.interaction import pause
from common.commander.resources import Resources

class Text:
    def __init__(self, name: str):
        self.fields: dict = Resources.Fields[name]
        self.p = Printer(name).act(print)

    def research(self, formula, initial):
        self.p.keys('Formula').args(formula).print()
        self.p.keys('Research').args(initial).print()

    def no_roots(self):
        self.p.keys('No roots').args().print()

    def roots(self, result):
        self.p.keys('Roots').args(result).print()

    def source(self, roots):
        fields = self.fields['Source'].copy()
        Table(fields).rows(roots).show()
        return self

    def result(self, *args):
        self.p.keys('Result').args(*args).print()

    def pause(self):
        pause()
