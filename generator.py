from typing import overload, Generic, TypeVar
from random import Random

T = TypeVar("T")
class IntGenerateInfo(Generic[T]):
    min: T
    max: T
    def __init__(self, min: T, max: T):
        self.min = min
        self.max = max

class Generator(Generic[T]):
    def generate(self, info: IntGenerateInfo, rnd: Random):
        return rnd.randint(info.min, info.max)
    

