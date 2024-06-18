from common.drawing.table.table import Table
from common.commander.resources import Resources

class Text:
    def __init__(self, name: str, key: str):
        self.fields = Resources.Fields[name]
        self.key = key

    def source(self, values: tuple):
        fields = self.fields[self.key]['Source'].copy()
        Table(fields).row(values).show()
        return self

    def result(self, values: list, formula: str = ''):
        fields = self.fields[self.key]['Result'].copy()
        if formula != '':
            fields[0] += f': {formula}'
            fields[6] = formula
        Table(fields).columns(0, values).floats('.8').show().pause()
