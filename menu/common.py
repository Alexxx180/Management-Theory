def from_formula(formula: str) -> list:
    args: list = []; coeffs: list = []

    for p1 in formula.split('+'):
        p2 = p1.split('-')
        coeffs.add(p2[0].strip())
        for i in range(1, len(p1)):
            coeffs.add('-' + p2[i].strip())

    for text in coeffs:
        i: int = p.index('p')
        if i == -1:
            args.append(int(p))
        else:
            args.append(int(p[:i]))
    # (1, 8, 32, 80, 100) # ...split
    #"A": "p3 + 2p2 + 2p + 1",
    #"B": "p4 + p3 + 3p2 + 2p + 1"
    return args



print("If the polynomial of the denominator of the system's characteristic equation (transfer function is given as: ")
print("a0*s^n + a1*s^(n-1) + ... + a(n-1)*s + an")
print("Enter the degree of the denominator polynomial")

degree = int(input('Degree: '))
coefficients = []
for x in range (0, degree+1):
    coefficient = int(input(str('Enter coefficient '+ 'a' + str(x) + ": ")))
    coefficients.append(int(coefficient))
print(coefficients)
print("To be stable, all of the system's denominator polynomial coefficients must be greater than zero")



