import math
import pandas as pd
import timeit

from Problems.Problem import Problem


def AckleyTwosCalculations(iterations, rng):
    d = {'iteration': range(1, iterations+1), 'solutions': [], 'fitness': []}

    begin = timeit.default_timer()
    for x in range(iterations):
        pro = AckleyTwos(rng, 30)
        fitness, vector = pro.calculate()

        d.get('solutions').append(vector)
        d.get('fitness').append(fitness)

    stop = timeit.default_timer()
    df = pd.DataFrame(data=d)
    return df, (stop-begin)*1000

class AckleyTwos(Problem):
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
            term1 = (20 / ((math.e**0.2) * math.sqrt( (float(self.x_n[i])**2.0 + float(self.x_n[i+1])**2.0)) / 2))
            term2 = math.e**(0.5*( math.cos( (2.0*math.pi*self.x_n[i]) + math.cos(2.0*math.pi*self.x_n[i+1]))))
            out = 20 + math.e - term1 - term2
            rolling_sum += (out)

        return rolling_sum, self.x_n
