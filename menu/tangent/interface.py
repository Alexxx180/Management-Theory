from common.flow.texts.tangent import Text
from common.commander.switch import View
from common.flow.canvas.tangent import canvas_from
from menu.tangent.solutions.functions import tangent, draw
from menu.tangent.solutions.research import Research

def TangentMethod(key: str, name: str, args: tuple):
    research = Research(key, name)
    research.start(args)

    derive = research.derives[0]

    text = Text(name)
    text.formula(research.formula)
    text.message(research.message)

    if len(research.roots) == 0:
        text.no_roots(args[0], args[1])
        return

    rows = tangent(args[2], research)
    orders = draw(rows, name, 100)

    if View('Table', name): text.result(rows)
    if View('Plots', name):
        canvas = canvas_from(key, name, derive, args)
        canvas.show(orders)

    text.pause()
