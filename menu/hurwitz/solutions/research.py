from sympy.abc import x
from common.commander.resources import Resources
from common.calculus.trigonometry import form, invokation, express

class Research:
    def __init__(self, key: str, name: str):
        self.a: list = []
        self.b: list = []
        self.formula: list = []
        self.derives: list = []
        self.text = Resources.Texts[name]

        formula = ('F', express(Resources.Formula[name][key]))
        for i in range(0, 3):
            formula = self.derive(formula)

        self.message: str = ''
        self.roots: tuple = ()

    def derive(self, formula) -> str:
        self.formula.append((formula[0] + '(x)', formula[1]))
        self.derives.append(invokation(formula[1], x))
        return (formula[0] + '’', form(formula[1], x))

    def side(self, key: str, d: tuple):
        if d[2] == 0 or d[3] == 0:
            self.problem('Derivatives', key, d[2], d[3])
        else:
            self.message = str(self.m)
            self.roots = (d[0], self.m)

    def problem(self, key: str, *args):
        self.message: str = self.text[key].format(*args)

    def descent(self, a: float, b: float):
        self.m: float = min(abs(self.a[2]), abs(self.b[2]))
        if a * self.a[3] > 0:
            self.side('a', self.a)
        elif b * self.b[2] > 0:
            self.side('b', self.b)
        else:
            self.problem('Problem', a, b, a * b)

    def start(self, ab: tuple):
        self.a.append(ab[0])
        self.b.append(ab[1])
        for derive in self.derives:
            self.a.append(derive(self.a[0]))
            self.b.append(derive(self.b[0]))

        a: float = self.a[1]
        b: float = self.b[1]
        if a * b < 0:
            self.descent(a, b)
        else:
            self.problem('Problem', a, b, a * b)
