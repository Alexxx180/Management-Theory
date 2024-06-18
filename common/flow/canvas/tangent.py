from common.calculus.objects.ends import Ends
from common.drawing.graphs.spaces.scatter import ScatterSpace
from common.drawing.graphs.builder import CanvasBuilder
from common.drawing.graphs.graphs import Graphs

def canvas_from(key: str, name: str, formula: callable, args: tuple):
    base: tuple = Ends(100).margin()

    graph = Graphs(1, 1)
    space = ScatterSpace(name)

    builder = CanvasBuilder()
    builder.space(space)
    builder.graph(graph)
    builder.formula(formula)

    for plane in (base, args):
        builder.mark(plane).plane()

    builder.label(f'Plot {key}')
    builder.entitle('Full Name')

    return builder.canvas
