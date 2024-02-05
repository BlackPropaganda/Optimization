import math
import pandas as pd
import timeit

from Problems.Problem import Problem


def SineEnvelopeCalculations(iterations, rng):

    d = {'iteration': range(1, iterations+1), 'solutions': [], 'fitness': []}

    begin = timeit.default_timer()
    for x in range(iterations):
        #
        ros = SineEnvelope(rng, 30)
        fitness, vector = ros.calculate()

        d.get('solutions').append(vector)
        d.get('fitness').append(fitness)
    
    stop = timeit.default_timer()
    df = pd.DataFrame(data=d)
    return df, (stop-begin)*1000

class SineEnvelope(Problem):
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
            numerator = math.sin(
                (
                    (self.x_n[i]**2) + (self.x_n[i+1]**2) - 0.5
                )**2
            )
            denominator = (
                1 + (
                    0.0001*( (self.x_n[i]**2) + (self.x_n[i+1]**2) )
                )
            )**2
            rolling_sum += (numerator/denominator)

        return rolling_sum, self.x_n
