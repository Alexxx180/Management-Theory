from menu.gauss.solutions.solutions import Gauss
from menu.gauss.solutions.checks import is_suitable
from common.handlers.interaction import pause

def GaussMethod(array, text):
    if is_suitable(array.shape):
        Gauss(array, text).system_elimination()
    else:
        text.no_solutions()
