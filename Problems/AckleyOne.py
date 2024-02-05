import math
import pandas as pd
import timeit

from Problems.Problem import Problem

def AckleyOnesCalculations(iterations, rng):

    d = {'iteration': range(1, iterations+1), 'solutions': [], 'fitness': []}

    begin = timeit.default_timer()
    for x in range(iterations):
        #
        ros = AckleyOnes(rng, 30)
        fitness, vector = ros.calculate()

        d.get('solutions').append(vector)
        d.get('fitness').append(fitness)
    
    stop = timeit.default_timer()
    df = pd.DataFrame(data=d)
    return df, (stop-begin)*1000

class AckleyOnes(Problem):
    def __init__(self, generator, dimensions) -> None:
        super().__init__(generator, dimensions)
        self.generate_sequence()
        
    
    def generate_sequence(self):
        for x in range(self.dimensions):
            self.x_n.append(self.generator.generate())


    def calculate(self):
        # Ask about this in class!
        rolling_sum = 0

        for i in range(len(self.x_n)-1):
            term1 = 1/(math.e**(0.2)) * math.sqrt((self.x_n[i]**2.0) + (self.x_n[i+1]**2.0))
            term2 = 3 * (math.cos(2*self.x_n[i]) + math.sin(2*self.x_n[i+1]))
            rolling_sum += term1 + term2

        return rolling_sum, self.x_n
