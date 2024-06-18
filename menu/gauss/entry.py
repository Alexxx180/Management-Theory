import numpy as np
from common.commander.switch import are_defaults
from common.commander.resources import Resources
from common.flow.texts.gauss import Text
from menu.gauss.interface.interface import GaussMethod
from menu.gauss.interface.input import InputLoop

def GaussEntry():
    name = 'Gauss'
    array = np.array(Resources.Defaults[name], dtype=float)

    text = Text(name)
    text.source(array)

    if are_defaults():
        GaussMethod(array, text)
    else:
        validator = InputLoop(text)
        if validator.perform():
            GaussMethod(validator.matrix, validator.text)

    text.pause()
