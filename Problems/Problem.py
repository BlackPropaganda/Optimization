class Problem:
    def __init__(self, generator, dimensions) -> None:
        self.generator = generator
        self.dimensions = dimensions
        self.x_n = []

    def generate_sequence(self):
        for x in range(self.dimensions):
            self.x_n.append(self.generator.generate())
    
    def calculate(self):
        pass

    def gradient_descent(self, delta):
        old_fitness, vector = self.calculate() # new_fitness value of current fitness
        # for i in range(len(self.x_n)):
        for i in range(len(self.x_n)):
            # walk down gradient
            while True:
                try:

                    # descend x_i by delta changing position.
                    self.x_n[i] = self.x_n[i] - delta

                    # if vector is less fit, break.
                    new_fitness, vector = self.calculate()
                    # print("new: ", new_fitness, "old:", old_fitness, "x_n", self.x_n[i])
                    if new_fitness >= old_fitness:
                        self.x_n[i] = self.x_n[i] + delta # replacing value with last best gradient
                        break
                    else:
                        old_fitness = new_fitness

                except ZeroDivisionError:
                    print("Warning: Division By Zero Detected. Defaulting to Value of One Delta above x_n.")
                    self.x_n[i] = self.x_n[i]+delta
                    break
            # walk up gradient
            while True:
                try:
                    # descend x_i by delta changing position.
                    self.x_n[i] = self.x_n[i] + delta

                    # if vector is less fit, break.
                    new_fitness, vector = self.calculate()
                    # print("new: ", new_fitness, "old:", old_fitness, "x_n:", self.x_n[i])
                    # print("new: ", new_fitness, "old:", old_fitness)
                    if new_fitness >= old_fitness:
                        self.x_n[i] = self.x_n[i] - delta # replacing value with last best gradient
                        break
                    else:
                        old_fitness = new_fitness

                except ZeroDivisionError:
                    print("Warning: Division By Zero Detected. Defaulting to Value of One Delta below x_n.")
                    self.x_n[i] = self.x_n[i]-delta
                    break

        return self.calculate()


    
                
                    
