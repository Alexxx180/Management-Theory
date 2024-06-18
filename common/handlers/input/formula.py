def from_formula(formula: str) -> list:
    args: list = []; c: list = []

    for p1 in formula.split('+'):
        p2 = p1.split('-')
        c.append(p2[0].strip())
        for i in range(1, len(p1)):
            c.append('-' + p2[i].strip())

    for text in c:
        i: int = p.index('p')
        if i == -1:
            args.append(int(p))
        else:
            args.append(int(p[:i]))

    # (1, 8, 32, 80, 100) # ...split
    #"A": "p3 + 2p2 + 2p + 1",
    #"B": "p4 + p3 + 3p2 + 2p + 1"

    return args
