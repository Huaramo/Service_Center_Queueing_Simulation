import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

# Queue are formed by the customers.
class Queue:
    def __init__(self, name, lsCustomers):
        self.name = name
        self.lsCustomers = lsCustomers
    
    def addCustomer(self, customer):
        self.lsCustomers.append(customer)

    def removeCustomer(self):
        out=self.lsCustomers.pop(0)
        return out
    def getCustomers(self):
        return self.lsCustomers

    def getQueueLength(self):
        return len(self.lsCustomers)













