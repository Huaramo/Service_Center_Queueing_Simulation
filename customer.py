import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

#The OOP models the queue in a service center.

# The class of a customer.
#It has a name with the format customer + No. .
#Customer can come in to the service center and wait in a queue.
#A customer comes in a service center with a time point A,
#then waits until time point B to be served.
#He/she does not leave until time point C.
#The number of the counter is used as the unit of the time point.
# A customer also has the probability of entering the service center.
class Customer:
    def __init__(self, name, arrival, departure, probEnter, probNow):
        self.name = name
        self.arrival=arrival
        self.departure = departure
        self.probEnter = probEnter
        self.probNow = probNow


    def isLinedUp(self):
        return self.probEnter >= self.probNow    

