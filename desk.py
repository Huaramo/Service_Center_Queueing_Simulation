import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from queue import Queue
import warnings
warnings.filterwarnings("ignore")

#Desk has desk number.
#Desk is occupied by a staff with a name, the efficiency of resolving the issue and the queue.
#Desk also has the probability of whether it can solve the issues of a customer per round.
class Desk:

    def __init__(self, name, efficiency, probNow, queue):
        self.name = name
        self.efficiency = efficiency
        self.probNow = probNow
        self.queue = queue
        
    def isSolved(self):
        return self.efficiency >= self.probNow

    def getQueue(self):
        return self.queue









