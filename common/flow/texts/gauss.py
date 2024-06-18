from common.drawing.table.table import Table
from common.handlers.interaction import pause
from common.handlers.printer import Printer
from common.commander.resources import Resources

class Text:
    def __init__(self, name: str):
        self.fields: dict = Resources.Fields[name]
        self.p = Printer(name)

    def empty(self, name: str, row: list):
        self.p.act(print).keys('Solutions', 'Common').args(row).print()
        self.p.edit(1, name).args().print()

    def zeros(self):
        self.p.act(print).keys('Solutions', 'Endless').args().print()

    def process(self):
        self.p.act(pause).keys('Input', 'Data').args().print()

    def single(self):
        self.p.act(pause).keys('Input', 'Single').args().print()

    def varying(self):
        self.p.act(pause).keys('Input', 'Count').args().print()

    def no_solutions(self):
        self.p.act(print).keys('Solutions', 'Not found').args().print()

    def description(self): return self.p.keys('Input', 'String').text()

    def reverse_step(self, *args):
        self.p.act(print).keys('Reverse', 'Step').args(*args).print()

    def reverse_course(self):
        self.p.act(print).keys('Reverse', 'Course').args().print()

    def straight_step(self, *args):
        self.p.act(print).keys('Straight', 'Step').args(*args).print()

    def straight_course(self):
        self.p.act(print).keys('Straight', 'Course').args().print()

    def source(self, array):
        Table(self.fields['Source'].copy()).align('Right').matrix(array).show()

    def result(self, result):
        Table().matrix(result).floats('.3').align('Right').show()

    def pause(self, text: str = ''):
        pause(text)
