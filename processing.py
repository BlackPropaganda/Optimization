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

from utils import *

def processSchwefels():
    print("="*30, "Schwefels", "="*30)
    scw = bulkSchwefels()
    scw_lcg = scw.get("lcg")
    scw_lcg[0].to_csv('out/lcg_scwefels.csv', ';')
    
    scw_mt = scw.get("mt")
    scw_mt[0].to_csv('out/mt_scwefels.csv', ';')

    print("lcg time:\t", scw_lcg[1])
    print("mt time:\t", scw_mt[1])

    print("===== LCG =====")
    # print(scw_mt[0])
    lcg_bf = find_best_fitness(scw_lcg[0])
    compile_statistics(scw_lcg[0])

    print("="*60)

    print("===== MT =====")
    # print(scw_mt[0])
    mt_bf = find_best_fitness(scw_mt[0])
    compile_statistics(scw_mt[0])

    print("==== Fitness Results ====")
    print("LCG best fitness:", lcg_bf)
    print("MT best fitness:", mt_bf)


    print("==== Gradient Descent ==== ")
    lcg_best = get_best_vector(scw_lcg[0])['solutions'].values[0]
    mt_best = get_best_vector(scw_mt[0])['solutions'].values[0]

    # RNG does not matter, their vectors are going to be overwritten
    lcg_temp = Schwefels(LCG_RNG(0,0), 30)
    mt_temp = Schwefels(LCG_RNG(0,0), 30)

    lcg_temp.x_n = lcg_best
    mt_temp.x_n = mt_best

    lcg_new_fitness, lcg_new_vector = lcg_temp.gradient_descent(1)
    mt_new_fitness, mt_new_vector = mt_temp.gradient_descent(1)

    print("LCG Gradient Descent Optimization Results:", lcg_new_fitness)
    print("Vector:", lcg_new_vector)

    print("MT Gradient Descent Optimization Results:", mt_new_fitness)
    print("Vector:", mt_new_vector)

    print("="*60)


def processDeJongs():
    print("="*30, "De Jong", "="*30)
    scw = bulkDeJongs()
    scw_lcg = scw.get("lcg")
    scw_lcg[0].to_csv('out/lcg_dejong.csv', ';')
    
    scw_mt = scw.get("mt")
    scw_mt[0].to_csv('out/mt_dejong.csv', ';')

    print("lcg time:\t", scw_lcg[1])
    print("mt time:\t", scw_mt[1])

    print("===== LCG =====")
    # print(scw_mt[0])
    lcg_bf = find_best_fitness(scw_lcg[0])
    compile_statistics(scw_lcg[0])

    print("="*60)

    print("===== MT =====")
    # print(scw_mt[0])
    mt_bf = find_best_fitness(scw_mt[0])
    compile_statistics(scw_mt[0])


    print("==== Fitness Results ====")
    print("LCG best fitness:", lcg_bf)
    print("MT best fitness:", mt_bf)


    print("==== Gradient Descent ==== ")
    lcg_best = get_best_vector(scw_lcg[0])['solutions'].values[0]
    mt_best = get_best_vector(scw_mt[0])['solutions'].values[0]

    # RNG does not matter, their vectors are going to be overwritten
    lcg_temp = DeJongs(LCG_RNG(0,0), 30)
    mt_temp = DeJongs(LCG_RNG(0,0), 30)

    lcg_temp.x_n = lcg_best
    mt_temp.x_n = mt_best

    lcg_new_fitness, lcg_new_vector = lcg_temp.gradient_descent(1)
    mt_new_fitness, mt_new_vector = mt_temp.gradient_descent(1)

    print("LCG Gradient Descent Optimization Results:", lcg_new_fitness)
    print("Vector:", lcg_new_vector)

    print("MT Gradient Descent Optimization Results:", mt_new_fitness)
    print("Vector:", mt_new_vector)

    print("="*60)

def processRosenbrock():
    print("="*30, "Rosenbrock", "="*30)
    scw = bulkRosenbrocks()
    scw_lcg = scw.get("lcg")
    scw_lcg[0].to_csv('out/lcg_rosenbrock.csv', ';')
    
    scw_mt = scw.get("mt")
    scw_mt[0].to_csv('out/mt_rosenbrock.csv', ';')

    print("lcg time:\t", scw_lcg[1])
    print("mt time:\t", scw_mt[1])

    print("===== LCG =====")
    # print(scw_mt[0])
    lcg_bf = find_best_fitness(scw_lcg[0])
    compile_statistics(scw_lcg[0])

    print("="*60)

    print("===== MT =====")
    # print(scw_mt[0])
    mt_bf = find_best_fitness(scw_mt[0])
    compile_statistics(scw_mt[0])

    print("==== Fitness Results ====")
    print("LCG best fitness:", lcg_bf)
    print("MT best fitness:", mt_bf)


    print("==== Gradient Descent ==== ")
    lcg_best = get_best_vector(scw_lcg[0])['solutions'].values[0]
    mt_best = get_best_vector(scw_mt[0])['solutions'].values[0]

    # RNG does not matter, their vectors are going to be overwritten
    lcg_temp = Rosenbrocks(LCG_RNG(0,0), 30)
    mt_temp = Rosenbrocks(LCG_RNG(0,0), 30)

    lcg_temp.x_n = lcg_best
    mt_temp.x_n = mt_best

    lcg_new_fitness, lcg_new_vector = lcg_temp.gradient_descent(1)
    mt_new_fitness, mt_new_vector = mt_temp.gradient_descent(1)

    print("LCG Gradient Descent Optimization Results:", lcg_new_fitness)
    print("Vector:", lcg_new_vector)

    print("MT Gradient Descent Optimization Results:", mt_new_fitness)
    print("Vector:", mt_new_vector)

    print("="*60)

def processRastrigin():
    print("="*30, "Rastrigin", "="*30)
    scw = bulkRastrigins()
    scw_lcg = scw.get("lcg")
    scw_lcg[0].to_csv('out/lcg_rastrigin.csv', ';')
    
    scw_mt = scw.get("mt")
    scw_mt[0].to_csv('out/mt_rastrigin.csv', ';')

    print("lcg time:\t", scw_lcg[1])
    print("mt time:\t", scw_mt[1])

    print("===== LCG =====")
    # print(scw_mt[0])
    lcg_bf = find_best_fitness(scw_lcg[0])
    compile_statistics(scw_lcg[0])

    print("="*60)

    print("===== MT =====")
    # print(scw_mt[0])
    mt_bf = find_best_fitness(scw_mt[0])
    compile_statistics(scw_mt[0])

    print("==== Fitness Results ====")
    print("LCG best fitness:", lcg_bf)
    print("MT best fitness:", mt_bf)


    print("==== Gradient Descent ==== ")
    lcg_best = get_best_vector(scw_lcg[0])['solutions'].values[0]
    mt_best = get_best_vector(scw_mt[0])['solutions'].values[0]

    # RNG does not matter, their vectors are going to be overwritten
    lcg_temp = Rastrigins(LCG_RNG(0,0), 30)
    mt_temp = Rastrigins(LCG_RNG(0,0), 30)

    lcg_temp.x_n = lcg_best
    mt_temp.x_n = mt_best

    lcg_new_fitness, lcg_new_vector = lcg_temp.gradient_descent(1)
    mt_new_fitness, mt_new_vector = mt_temp.gradient_descent(1)

    print("LCG Gradient Descent Optimization Results:", lcg_new_fitness)
    print("Vector:", lcg_new_vector)

    print("MT Gradient Descent Optimization Results:", mt_new_fitness)
    print("Vector:", mt_new_vector)


    print("="*60)

def processGriewangk():
    print("="*30, "Griewangk", "="*30)
    scw = bulkGrewangks()
    scw_lcg = scw.get("lcg")
    scw_lcg[0].to_csv('out/lcg_griewangk.csv', ';')
    
    scw_mt = scw.get("mt")
    scw_mt[0].to_csv('out/mt_griewangk.csv', ';')

    print("lcg time:\t", scw_lcg[1])
    print("mt time:\t", scw_mt[1])

    print("===== LCG =====")
    # print(scw_mt[0])
    lcg_bf = find_best_fitness(scw_lcg[0])
    compile_statistics(scw_lcg[0])

    print("="*60)

    print("===== MT =====")
    # print(scw_mt[0])
    mt_bf = find_best_fitness(scw_mt[0])
    compile_statistics(scw_mt[0])

    print("==== Fitness Results ====")
    print("LCG best fitness:", lcg_bf)
    print("MT best fitness:", mt_bf)


    print("==== Gradient Descent ==== ")
    lcg_best = get_best_vector(scw_lcg[0])['solutions'].values[0]
    mt_best = get_best_vector(scw_mt[0])['solutions'].values[0]

    # RNG does not matter, their vectors are going to be overwritten
    lcg_temp = Griewangks(LCG_RNG(0,0), 30)
    mt_temp = Griewangks(LCG_RNG(0,0), 30)

    lcg_temp.x_n = lcg_best
    mt_temp.x_n = mt_best

    lcg_new_fitness, lcg_new_vector = lcg_temp.gradient_descent(1)
    mt_new_fitness, mt_new_vector = mt_temp.gradient_descent(1)

    print("LCG Gradient Descent Optimization Results:", lcg_new_fitness)
    print("Vector:", lcg_new_vector)

    print("MT Gradient Descent Optimization Results:", mt_new_fitness)
    print("Vector:", mt_new_vector)

    print("="*60)

def processSineEnvelope():
    print("="*30, "Sine Envelope", "="*30)
    scw = bulkSineEnvelope()
    scw_lcg = scw.get("lcg")
    scw_lcg[0].to_csv('out/lcg_sine_envelope.csv', ';')
    
    scw_mt = scw.get("mt")
    scw_mt[0].to_csv('out/mt_sine_envelope.csv', ';')

    print("lcg time:\t", scw_lcg[1])
    print("mt time:\t", scw_mt[1])

    print("===== LCG =====")
    # print(scw_mt[0])
    lcg_bf = find_best_fitness(scw_lcg[0])
    compile_statistics(scw_lcg[0])

    print("="*60)

    print("===== MT =====")
    # print(scw_mt[0])
    mt_bf = find_best_fitness(scw_mt[0])
    compile_statistics(scw_mt[0])

    print("==== Fitness Results ====")
    print("LCG best fitness:", lcg_bf)
    print("MT best fitness:", mt_bf)


    print("==== Gradient Descent ==== ")
    lcg_best = get_best_vector(scw_lcg[0])['solutions'].values[0]
    mt_best = get_best_vector(scw_mt[0])['solutions'].values[0]

    # RNG does not matter, their vectors are going to be overwritten
    lcg_temp = SineEnvelope(LCG_RNG(0,0), 30)
    mt_temp = SineEnvelope(LCG_RNG(0,0), 30)

    lcg_temp.x_n = lcg_best
    mt_temp.x_n = mt_best

    lcg_new_fitness, lcg_new_vector = lcg_temp.gradient_descent(1)
    mt_new_fitness, mt_new_vector = mt_temp.gradient_descent(1)

    print("LCG Gradient Descent Optimization Results:", lcg_new_fitness)
    print("Vector:", lcg_new_vector)

    print("MT Gradient Descent Optimization Results:", mt_new_fitness)
    print("Vector:", mt_new_vector)

    print("="*60)

def processStretchedVSine():
    print("="*30, "Stretched V Sine", "="*30)
    scw = bulkSineEnvelope()
    scw_lcg = scw.get("lcg")
    scw_lcg[0].to_csv('out/lcg_stretched_sine.csv', ';')
    
    scw_mt = scw.get("mt")
    scw_mt[0].to_csv('out/mt_stretched_sine.csv', ';')

    print("lcg time:\t", scw_lcg[1])
    print("mt time:\t", scw_mt[1])

    print("===== LCG =====")
    # print(scw_mt[0])
    lcg_bf = find_best_fitness(scw_lcg[0])
    compile_statistics(scw_lcg[0])

    print("="*60)

    print("===== MT =====")
    # print(scw_mt[0])
    mt_bf = find_best_fitness(scw_mt[0])
    compile_statistics(scw_mt[0])

    print("==== Fitness Results ====")
    print("LCG best fitness:", lcg_bf)
    print("MT best fitness:", mt_bf)


    print("==== Gradient Descent ==== ")
    lcg_best = get_best_vector(scw_lcg[0])['solutions'].values[0]
    mt_best = get_best_vector(scw_mt[0])['solutions'].values[0]

    # RNG does not matter, their vectors are going to be overwritten
    lcg_temp = StretchedVSines(LCG_RNG(0,0), 30)
    mt_temp = StretchedVSines(LCG_RNG(0,0), 30)

    lcg_temp.x_n = lcg_best
    mt_temp.x_n = mt_best

    lcg_new_fitness, lcg_new_vector = lcg_temp.gradient_descent(1)
    mt_new_fitness, mt_new_vector = mt_temp.gradient_descent(1)

    print("LCG Gradient Descent Optimization Results:", lcg_new_fitness)
    print("Vector:", lcg_new_vector)

    print("MT Gradient Descent Optimization Results:", mt_new_fitness)
    print("Vector:", mt_new_vector)

    print("="*60)

def processAckleysOne():
    print("="*30, "Ackleys One", "="*30)
    scw = BulkAckleyOnes()
    scw_lcg = scw.get("lcg")
    scw_lcg[0].to_csv('out/lcg_ackleys_one.csv', ';')
    
    scw_mt = scw.get("mt")
    scw_mt[0].to_csv('out/mt_ackleys_one.csv', ';')

    print("lcg time:\t", scw_lcg[1])
    print("mt time:\t", scw_mt[1])

    print("===== LCG =====")
    # print(scw_mt[0])
    lcg_bf = find_best_fitness(scw_lcg[0])
    compile_statistics(scw_lcg[0])

    print("="*60)

    print("===== MT =====")
    # print(scw_mt[0])
    mt_bf = find_best_fitness(scw_mt[0])
    compile_statistics(scw_mt[0])

    print("==== Fitness Results ====")
    print("LCG best fitness:", lcg_bf)
    print("MT best fitness:", mt_bf)


    print("==== Gradient Descent ==== ")
    lcg_best = get_best_vector(scw_lcg[0])['solutions'].values[0]
    mt_best = get_best_vector(scw_mt[0])['solutions'].values[0]

    # RNG does not matter, their vectors are going to be overwritten
    lcg_temp = AckleyOnes(LCG_RNG(0,0), 30)
    mt_temp = AckleyOnes(LCG_RNG(0,0), 30)

    lcg_temp.x_n = lcg_best
    mt_temp.x_n = mt_best

    lcg_new_fitness, lcg_new_vector = lcg_temp.gradient_descent(1)
    mt_new_fitness, mt_new_vector = mt_temp.gradient_descent(1)

    print("LCG Gradient Descent Optimization Results:", lcg_new_fitness)
    print("Vector:", lcg_new_vector)

    print("MT Gradient Descent Optimization Results:", mt_new_fitness)
    print("Vector:", mt_new_vector)
    print("="*60)


def processAckleysTwo():
    print("="*30, "Ackleys Two", "="*30)
    scw = BulkAckleyTwos()
    scw_lcg = scw.get("lcg")
    scw_lcg[0].to_csv('out/lcg_ackleys_two.csv', ';')
    
    scw_mt = scw.get("mt")
    scw_mt[0].to_csv('out/mt_ackleys_two.csv', ';')

    print("lcg time:\t", scw_lcg[1])
    print("mt time:\t", scw_mt[1])

    print("===== LCG =====")
    # print(scw_mt[0])
    lcg_bf = find_best_fitness(scw_lcg[0])
    compile_statistics(scw_lcg[0])

    print("="*60)

    print("===== MT =====")
    # print(scw_mt[0])
    mt_bf = find_best_fitness(scw_mt[0])
    compile_statistics(scw_mt[0])

    print("==== Fitness Results ====")
    print("LCG best fitness:", lcg_bf)
    print("MT best fitness:", mt_bf)


    print("==== Gradient Descent ==== ")
    lcg_best = get_best_vector(scw_lcg[0])['solutions'].values[0]
    mt_best = get_best_vector(scw_mt[0])['solutions'].values[0]

    # RNG does not matter, their vectors are going to be overwritten
    lcg_temp = AckleyTwos(LCG_RNG(0,0), 30)
    mt_temp = AckleyTwos(LCG_RNG(0,0), 30)

    lcg_temp.x_n = lcg_best
    mt_temp.x_n = mt_best

    lcg_new_fitness, lcg_new_vector = lcg_temp.gradient_descent(1)
    mt_new_fitness, mt_new_vector = mt_temp.gradient_descent(1)

    print("LCG Gradient Descent Optimization Results:", lcg_new_fitness)
    print("Vector:", lcg_new_vector)

    print("MT Gradient Descent Optimization Results:", mt_new_fitness)
    print("Vector:", mt_new_vector)

    print("="*60)


def processEggHolder():
    print("="*30, "Egg Holder", "="*30)
    scw = BulkEggholders()
    scw_lcg = scw.get("lcg")
    scw_lcg[0].to_csv('out/lcg_eggholder.csv', ';')
    
    scw_mt = scw.get("mt")
    scw_mt[0].to_csv('out/mt_eggholder.csv', ';')

    print("lcg time:\t", scw_lcg[1])
    print("mt time:\t", scw_mt[1])

    print("===== LCG =====")
    # print(scw_mt[0])
    lcg_bf = find_best_fitness(scw_lcg[0])
    compile_statistics(scw_lcg[0])

    print("="*60)

    print("===== MT =====")
    # print(scw_mt[0])
    mt_bf = find_best_fitness(scw_mt[0])
    compile_statistics(scw_mt[0])
    print("==== Fitness Results ====")
    print("LCG best fitness:", lcg_bf)
    print("MT best fitness:", mt_bf)

    print("==== Gradient Descent ==== ")
    lcg_best = get_best_vector(scw_lcg[0])['solutions'].values[0]
    mt_best = get_best_vector(scw_mt[0])['solutions'].values[0]

    # RNG does not matter, their vectors are going to be overwritten
    lcg_temp = Eggholders(LCG_RNG(0,0), 30)
    mt_temp = Eggholders(LCG_RNG(0,0), 30)

    lcg_temp.x_n = lcg_best
    mt_temp.x_n = mt_best

    lcg_new_fitness, lcg_new_vector = lcg_temp.gradient_descent(1)
    mt_new_fitness, mt_new_vector = mt_temp.gradient_descent(1)

    print("LCG Gradient Descent Optimization Results:", lcg_new_fitness)
    print("Vector:", lcg_new_vector)

    print("MT Gradient Descent Optimization Results:", mt_new_fitness)
    print("Vector:", mt_new_vector)

    print("="*60)