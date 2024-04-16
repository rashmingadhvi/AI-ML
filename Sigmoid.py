import math


class Sigmoid(object):
    def __init__(self, x:int) -> None:
        self.x = x

    def calculate(self) -> float:
        return 1 / (1+math.exp(-self.x))



