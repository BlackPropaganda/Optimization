from Problems.Schwefels import Schwefels, SchwefelsCalculations
from utils import *
from processing import *

from threading import Lock, Thread
import pandas as pd

import sys
import warnings

warnings.filterwarnings("ignore")

DIMENSIONS = 30

if __name__ == "__main__":
    
    if input("Warning: This will generate all outputs for the project and wipe local CSV Data. Proceed? Y/n:").lower() == 'y':
        processSchwefels()
        processDeJongs()
        processRosenbrock()
        processRastrigin()
        processGriewangk()
        processSineEnvelope()
        processStretchedVSine()
        processAckleysOne()
        processAckleysTwo()
        processEggHolder()
    else:
        print("Experiment Aborted.")
