import math
import pandas as pd
import timeit

from Problems.Problem import Problem


def SchwefelsCalculations(iterations, rng):

    d = {'iteration': range(1, iterations+1), 'solutions': [], 'fitness': []}

    begin = timeit.default_timer()
    for x in range(iterations):
        scw = Schwefels(rng, 30)
        fitness, vector = scw.calculate()

        d.get('solutions').append(vector)
        d.get('fitness').append(fitness)
    stop = timeit.default_timer()
    df = pd.DataFrame(data=d)
    return df, (stop-begin)*1000



class Schwefels(Problem):
    def __init__(self, generator, dimensions) -> None:
        super().__init__(generator, dimensions)
        self.generate_sequence()
    
    def generate_sequence(self):
        for x in range(self.dimensions):
            self.x_n.append(self.generator.generate())


    def calculate(self):
        output_vector = []
        for x_i in self.x_n:
            # Square root of abs value of x_n
            out = math.fabs(x_i)
            out = math.sqrt(out)
            out = (math.fabs(x_i))*math.sin(out)
            # now converting to radians
            # out = math.radians(out)
            output_vector.append(out)

        # summating all calculated values
        vector_sum = sum(output_vector)

        # scaling the output, then subtracting.
        scale = 418.9839*self.dimensions
        return (scale - vector_sum), self.x_n
