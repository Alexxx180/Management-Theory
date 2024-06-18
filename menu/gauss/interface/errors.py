class Errors:
    def __init__(self, errors: tuple):
        self.keys: tuple = errors
        self.total: bool = True
        self.at: dict = {}
        for error in errors: self.at[error] = False

    def __apply(self, appliers: tuple, i: int):
        key: str = self.keys[i]
        self.at[key] = appliers[i]()
        self.total = self.total or self.at[key]

    def compute(self, appliers: tuple) -> bool:
        self.total = False
        i: int = 0

        while not self.total and i < len(appliers):
            self.__apply(appliers, i)
            i = i + 1
