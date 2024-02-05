import math
import pandas as pd
import timeit

from Problems.Problem import Problem


def GriewangksCalculations(iterations, rng):

    d = {'iteration': range(1, iterations+1), 'solutions': [], 'fitness': []}

    begin = timeit.default_timer()
    for x in range(iterations):
        #
        ros = Griewangks(rng, 30)
        fitness, vector = ros.calculate()

        d.get('solutions').append(vector)
        d.get('fitness').append(fitness)
    
    stop = timeit.default_timer()
    df = pd.DataFrame(data=d)
    return df, (stop-begin)*1000

class Griewangks(Problem):
    def __init__(self, generator, dimensions) -> None:
        super().__init__(generator, dimensions)
        self.generate_sequence()
        
    
    def generate_sequence(self):
        for x in range(self.dimensions):
            self.x_n.append(self.generator.generate())


    def calculate(self):
        sum_component = 0
        prod_component = 1

        # sum component
        for x_i in self.x_n:
            sum_component += x_i**2 / 4000

        # product component 

        for i, x_i in enumerate(self.x_n, 1):
            prod_component *= math.cos((x_i/math.sqrt(i)))

        output = 1 + sum_component - prod_component

        return output, self.x_n
