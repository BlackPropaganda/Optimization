from time import time
# importing matplotlib 


# python module driver for the c implemented rand function

import ctypes

# Load the shared library into ctypes
lib = ctypes.CDLL('./LCG/lcg.dll')  # Use 'random_number.dll' on Windows

# ====================== random_number ===================== 
# return values for random_number
lib.random_number.restype = ctypes.c_int

# Argument type for random_number function
lib.random_number.argtypes = [ctypes.c_longdouble]

# ====================== random_range ======================
# return values for random_number
lib.random_range.restype = ctypes.c_int

# Argument type for random_number function
lib.random_range.argtypes = [ctypes.c_longdouble, ctypes.c_int, ctypes.c_int]



# unix epoch of a time I was working on this project
LCG_SEED = 1706166290.8088646


''' Class implementation for use in higher-level applications '''
class LCG_RNG:
    def __init__(self, min, max) -> None:
        self.MIN = min
        self.MAX = max
        pass

    def generate(self):
        return self.LCG_random_range()

    def LCG_rand(self):
        return lib.random_number(LCG_SEED)

    def LCG_random_range(self):
        return lib.random_range(LCG_SEED, self.MIN, self.MAX)




'''Proof of concept Main method prints ten random numbers between variable range.'''

'''
if __name__ == "__main__":
    for x in range (10):
        # print(LCG_rand())
        print(LCG_random_range())
'''