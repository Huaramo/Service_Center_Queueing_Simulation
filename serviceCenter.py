import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from customer import Customer
from queue import Queue
from desk import Desk
import warnings
warnings.filterwarnings("ignore")


# The class of a service center.
# A service center has multiple service desks to serve the customers
# Service Center has also queues for all desks....

class ServiceCenter:
    def __init__(self, name, lsDesks, durationOpening):
        self.name = name
        self.lsDesks = lsDesks
        self.durationOpening = durationOpening
        #self.Graphics = Graphics

    def addDesk(self, desk):
        self.lsDesks.append(desk)

    def extendDurationOpening():
        self.durationOpening = self.durationOpening + 1

    def getLsDesks(self):
        return self.lsDesks

    def getDurationOpening(self):
        return self.durationOpening
    
    

    def open(self):
        #Procedure of simulation is simple:
        #Within the duration of opening, one customer is added into the service center in any possible queue at a time.
        # Scan through each desk,
        # Which queue is being added with a customer is depend on the probability that is assigned to this customer.
        # Which queue that will be poped out one customer is also depend on the probability that is assigned to its corresponding desk.
        # If there is still customer left, then keep dealing with the customers until all customers leave the service center. 
        # Print each round of information. (Implemented later...)
        # The probability that a customer enters a queue is depend on the length of the queue with the following relationship:
        # probEnter = 1/log2(queueLength+1)

        print('-------------------')
        print(self.name)
        print('-------------------')
        print()
        for i in range(self.getDurationOpening()):
            print('Time lapse: ' + str(i))
            
            for desk in self.getLsDesks():
                
                tmpCustomer = Customer('Customer '+str(i), i, i, 0., 0.)
                tmpCustomer.probEnter = 1./np.log2(desk.queue.getQueueLength()+2)
                tmpCustomer.probNow = np.random.uniform(0, 1, 1)
                desk.probNow = np.random.uniform(0, 1, 1)
                if tmpCustomer.isLinedUp():
                    desk.queue.addCustomer(tmpCustomer)

                if desk.isSolved() and desk.queue.getQueueLength():
                    left_customer=desk.getQueue().removeCustomer()
                    left_customer.departure = i
                print('The number of customers before desk No. '+ desk.name + ' is amount to: ' + str(desk.queue.getQueueLength()))
                
                    
                

        print('The situation after the service hour: ')
        for desk in self.getLsDesks():
            for i in range(desk.getQueue().getQueueLength()):
                
                desk.probNow = np.random.uniform(0, 1, 1) 
                if desk.isSolved() and desk.queue.getQueueLength():
                    leftCustomer=desk.getQueue().removeCustomer()
                print('The number of customers before desk No. '+ desk.name + ' is amount to: ' + str(desk.queue.getQueueLength()))







