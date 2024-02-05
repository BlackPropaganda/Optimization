import timeit
import pandas as pd

from LCG.LCG import LCG_RNG
from MT.MT import MT_RNG
from UDEV.UDEV import UDEV

# Importing problem definitions
from Problems.Schwefels import Schwefels, SchwefelsCalculations
from Problems.DeJong import DeJongs, DeJongsCalculations
from Problems.Rosenbrock import Rosenbrocks, RosenbrockCalculations
from Problems.Rastrigin import Rastrigins, RastriginsCalculations
from Problems.Griewangk import Griewangks, GriewangksCalculations
from Problems.SineEnvelope import SineEnvelope, SineEnvelopeCalculations
from Problems.StretchedVSine import StretchedVSines, StretchedVSineCalculations
from Problems.AckleyOne import AckleyOnes, AckleyOnesCalculations
from Problems.AckleyTwo import AckleyTwos, AckleyTwosCalculations
from Problems.Eggholders import Eggholders, EggholdersCalculations

''' Returns output of a function and the time it took to get it in miliseconds'''
def timeExec(function, *args, **kwargs):
    begin = timeit.default_timer()
    ret = function(*args, **kwargs)
    stop = timeit.default_timer()
    return ret, (stop-begin)*1000

def find_best_fitness(df, attr="fitness"):
    return df[attr].min()

def get_best_vector(df, attr="fitness"):
    return df[df[attr]==df[attr].min()]

''' Statistics Portion '''

def get_average(df, attr="fitness"):
    return df[attr].mean()

# std. Deviation
def get_std_deviation(df, attr="fitness"):
    return df[attr].std()

# median
def get_median(df, attr="fitness"):
    return df[attr].median()

# range
def get_range(df, attr="fitness"):
    return df[attr].max() - df[attr].min()


def compile_statistics(df):
    avg = get_average(df)
    std_dev = get_std_deviation(df)
    med = get_median(df)
    range_ = get_range(df)
    print("Average:\t\t", avg)
    print("Standard Deviation:\t", std_dev)
    print("Median:\t\t\t", med)
    print("Range:\t\t\t", range_)

    return {
        "average": avg,
        "standard_deviation": std_dev,
        "median": med,
        "range_": range_
    }

''' Calculations Portion'''




'''Scwefels function'''
def test_scwefels():
    minimum = -500
    maximum = 500
    mt = MT_RNG(minimum, maximum)
    scw = Schwefels(mt, 30)
    scw.generate_sequence()
    val, time = timeExec(scw.gradient_descent, 2)

''' Rastrigin Test'''
def test_rastrigin():
    minimum = -30
    maximum = 30
    mt = MT_RNG(minimum, maximum)
    rast = Rastrigins(mt, 5)
    rast.x_n = [0]*5
    fitness, vector = rast.calculate()
    print(fitness, vector)

''' Test Ackleys 2'''
def test_ackleys_2():
    minimum = -32
    maximum = 32
    mt = MT_RNG(minimum, maximum)
    rast = AckleyTwos(mt, 2)
    rast.x_n = [0, -23]
    fitness, vector = rast.calculate()
    print(fitness, vector)

''' Test Eggholder '''
def test_eggholder():
    minimum = -500
    maximum = 500
    mt = MT_RNG(minimum, maximum)
    egg = Eggholders(mt, 2)
    egg.x_n = [512, 404.2319]
    fitness, vector = egg.calculate()
    print(fitness, vector)


''' Bulk calculations '''
def bulkSchwefels():
    minimum = -500
    maximum = 500
    mt = MT_RNG(minimum, maximum)
    lcg = LCG_RNG(minimum, maximum)

    outputs = {
        "mt": SchwefelsCalculations(30, mt),
        "lcg": SchwefelsCalculations(30, lcg)
    }
    return outputs

def bulkDeJongs():
    minimum = -100
    maximum = 100
    udev = UDEV(minimum, maximum)
    mt = MT_RNG(minimum, maximum)
    lcg = LCG_RNG(minimum, maximum)

    outputs = {
        "mt": DeJongsCalculations(30, mt),
        "lcg": DeJongsCalculations(30, lcg)
    }
    return outputs

def bulkRastrigins():
    minimum = -30
    maximum = 30

    udev = UDEV(minimum, maximum)
    mt = MT_RNG(minimum, maximum)
    lcg = LCG_RNG(minimum, maximum)

    outputs = {
        "mt": DeJongsCalculations(30, mt),
        "lcg": DeJongsCalculations(30, lcg)
    }
    return outputs

def bulkRosenbrocks():
    minimum = -100
    maximum = 100

    udev = UDEV(minimum, maximum)
    mt = MT_RNG(minimum, maximum)
    lcg = LCG_RNG(minimum, maximum)

    outputs = {
        "mt": RosenbrockCalculations(30, mt),
        "lcg": RosenbrockCalculations(30, lcg)
        }
    return outputs

def bulkGrewangks():
    minimum = -500
    maximum = 500

    mt = MT_RNG(minimum, maximum)
    lcg = LCG_RNG(minimum, maximum)

    outputs = {
        "mt": GriewangksCalculations(30, mt),
        "lcg": GriewangksCalculations(30, lcg)
    }
    return outputs

def bulkSineEnvelope():
    minimum = -30
    maximum = 30

    mt = MT_RNG(minimum, maximum)
    lcg = LCG_RNG(minimum, maximum)

    outputs = {
        "mt": SineEnvelopeCalculations(30, mt),
        "lcg": SineEnvelopeCalculations(30, lcg)
    }
    return outputs

def buklkStretchedVSine():
    minimum = -30
    maximum = 30

    mt = MT_RNG(minimum, maximum)
    lcg = LCG_RNG(minimum, maximum)

    outputs = {
        "mt": StretchedVSineCalculations(30, mt),
        "lcg": StretchedVSineCalculations(30, lcg)
    }

    return outputs

def BulkAckleyOnes():
    minimum = -32
    maximum = 32

    mt = MT_RNG(minimum, maximum)
    lcg = LCG_RNG(minimum, maximum)

    outputs = {
        "mt": AckleyOnesCalculations(30, mt),
        "lcg": AckleyOnesCalculations(30, lcg)
    }
    return outputs

def BulkAckleyTwos():
    minimum = -32
    maximum = 32

    mt = MT_RNG(minimum, maximum)
    lcg = LCG_RNG(minimum, maximum)

    outputs = {
        "mt": AckleyOnesCalculations(30, mt),
        "lcg": AckleyOnesCalculations(30, lcg)
    }
    return outputs

def BulkEggholders():
    minimum = -500
    maximum = 500

    mt = MT_RNG(minimum, maximum)
    lcg = LCG_RNG(minimum, maximum)

    outputs = {
        "mt": AckleyOnesCalculations(30, mt),
        "lcg": AckleyOnesCalculations(30, lcg)
    }
    return outputs
