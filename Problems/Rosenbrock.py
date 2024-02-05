import math
import pandas as pd
import timeit

from Problems.Problem import Problem


def RosenbrockCalculations(iterations, rng):

    d = {'iteration': range(1, iterations+1), 'solutions': [], 'fitness': []}

    begin = timeit.default_timer()
    for x in range(iterations):
        #
        ros = Rosenbrocks(rng, 30)
        fitness, vector = ros.calculate()

        d.get('solutions').append(vector)
        d.get('fitness').append(fitness)
    
    stop = timeit.default_timer()
    df = pd.DataFrame(data=d)
    return df, (stop-begin)*1000

class Rosenbrocks(Problem):
    def __init__(self, generator, dimensions) -> None:
        super().__init__(generator, dimensions)
        self.generate_sequence()
        
    
    def generate_sequence(self):
        for x in range(self.dimensions):
            self.x_n.append(self.generator.generate())


    def calculate(self):
        solution_vector = []

        for i in range(len(self.x_n)-1):
            out = 100 * math.pow((self.x_n[i+1] - math.pow(self.x_n[i], 2)), 2)
            out += math.pow((self.x_n[i]-1), 2)
            solution_vector.append(out)

        vector_sum = sum(solution_vector)
        return vector_sum, self.x_n
