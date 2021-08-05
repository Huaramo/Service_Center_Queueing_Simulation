import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from customer import Customer
from serviceCenter import ServiceCenter
from queue import Queue
from desk import Desk
import warnings
warnings.filterwarnings("ignore")


if __name__ == "__main__":
    #Initialize the service center with customers and desks:
    customer01 = Customer("Customer01", 0, 0, 0.5, 0.)
    customer02 = Customer("Customer02", 0, 0, 0.4, 0.)
    customer03 = Customer("Customer03", 0, 0, 0.3, 0)
    customer04 = Customer("Customer04", 0, 0, 0.2, 0)
    customer05 = Customer("Customer05", 0, 0, 0.1, 0)
    customer06 = Customer("Customer06", 0, 0, 0.4, 0)
    
    desk1 = Desk("Desk 1", 0.8, 1., Queue("Queue 1", [customer01, customer02]))   
    desk2 = Desk("Desk 2", 0.7, 1., Queue("Queue 2", [customer03, customer04]))
    desk3 = Desk("Desk 3", 0.6, 1., Queue("Queue 3", [customer05, customer06]))
    
    serviceCenter = ServiceCenter('Nostro Abbigliamento', [desk1, desk2, desk3], 2000) 
    serviceCenter.open()








