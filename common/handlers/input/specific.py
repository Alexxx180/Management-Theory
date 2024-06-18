from inquirer import prompt, Text
from common.commander.resources import Resources
from common.commander.switch import swap_instead_repeat
from common.handlers.input.validate import specify, number
from common.handlers.input.list import listing
from common.handlers.printer import Printer

errors = Printer('Common').act(print)

def validate_e() -> float:
    precision: callable = lambda e: abs(e) >= 1 or e < 1e-15 or e == 0.0
    return specify(float, precision, ('e', 0.0), 'Wrong e')

def request_n(start: int, end: int) -> int:
    count: callable = lambda n: n < start or n > end
    return specify(int, count, ('n', 0), 'Wrong n', start, end)

def pair(convert: callable, start: str, end: str):
    query: callable = lambda name: convert(prompt(Resources.Queries[name])[name])
    a, b = query(start), query(end)

    while b < a:
        if swap_instead_repeat():
            a, b = b, a
        else:
            a, b = query(start), query(end)

    return (a, b)

def setup_input(queries: dict):
    for argument, message in queries.items():
        Resources.Queries[argument] = [Text(argument, message=message, validate=number)]

    Resources.Input = {
        'Division': lambda: listing((float, ('a', 'b')), validate_e),
        'Tangent': lambda: listing((float, ('a', 'b')), validate_e),
        'Simpson': lambda b: listing((float, ('a', b)), lambda: pair(float, 'ₐ', 'ᵇ'), validate_e),
        'Runge': {
            'A': lambda: listing((float, ('x', 'y', 'h')), lambda: request_n(0, 100)),
            'B': lambda: listing((float, ('a', 'b', 'x', 'y', 'y’', 'h')), lambda: request_n(0, 100))
        }
    }
