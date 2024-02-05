# function implementing the native MT algorithm for Python
from time import time
from random import *

MT_SEED = 1706166290.8088646
RNG = Random()
# Fixed Seed
# RNG.seed(MT_SEED)
# Dynamic Seed
RNG.seed(time())

''' Class implementation for use in higher-level applications'''
class MT_RNG:
    def __init__(self, min_, max_) -> None:
        self.MIN = min_
        self.MAX = max_
        pass

    def MT_RAND(self):
        return RNG.randrange(self.MIN, self.MAX)

    def generate(self):
        return self.MT_RAND()

'''
if __name__ == "__main__":
    for x in range(100):
        print(MT_RAND())
'''