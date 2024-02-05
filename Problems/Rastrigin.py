import math
import pandas as pd
import timeit

from Problems.Problem import Problem


def RastriginsCalculations(iterations, rng):

    d = {'iteration': range(1, iterations+1), 'solutions': [], 'fitness': []}

    begin = timeit.default_timer()
    for x in range(iterations):
        #
        dej = Rastrigins(rng, 30)
        fitness, vector = dej.calculate()

        d.get('solutions').append(vector)
        d.get('fitness').append(fitness)
    
    stop = timeit.default_timer()
    df = pd.DataFrame(data=d)
    return df, (stop-begin)*1000

class Rastrigins(Problem):
    def __init__(self, generator, dimensions) -> None:
        super().__init__(generator, dimensions)
        self.generate_sequence()
        
    
    def generate_sequence(self):
        for x in range(self.dimensions):
            self.x_n.append(self.generator.generate())


    def calculate(self):
        solution_vector = []
        for x_i in self.x_n:
            # adding x_i squared to output
            out = ((x_i**2) - (10 * math.cos(
                (2*math.pi*x_i)
            )))
            solution_vector.append(out)


        # summating all calculated values
        vector_sum = sum(solution_vector)

        # scaling
        vector_sum *= (self.dimensions)
        vector_sum *= 10

        return vector_sum, self.x_n
