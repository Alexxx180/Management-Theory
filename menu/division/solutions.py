from common.calculus.objects.ends import Ends

class SegmentDivision:
    def __init__(self, args: tuple, derive: callable):
        self.roots: list = []
        self.orders: list = []
        self.a: float = args[0]
        self.b: float = args[1]
        self.e: float = args[2]
        self.formula: callable = derive

    def __root(self, i: int, y: float, color: str):
        root: tuple = (i, self.a, self.b)
        self.roots.append(root)

        order: tuple = (self.c, y, color)
        self.orders.append(order)

    def __not_found(self) -> bool:
        return self.b - self.a > self.e

    def __middle(self) -> float:
        return (self.a + self.b) / 2

    def __calculate(self) -> float:
        self.c = self.__middle()

        x: float = self.formula(self.a)
        y: float = self.formula(self.c)

        if x * y > 0:
            self.a = self.c
        else:
            self.b = self.c

        return y

    def study(self):
        self.e *= 2
        self.c: float
        i: int = 1

        while self.__not_found():
            y = self.__calculate()
            color: str = 'blue' if y < 0 else 'red'
            self.__root(i, y, color)
            i += 1

        y = self.__calculate()
        self.__root(i, y, 'green')
        self.c = self.__middle()

coeff = (1, 8, 32, 80, 100) # ...split

print('System is Not Stable')

if all(coeff) == 0:
    return False

count = len(coeff)
columns = math.ceil(len / 2)






































