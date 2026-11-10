import exo1
import matplotlib.pyplot as plt
import numpy as np

def initialize_centers(X,k):

    centres = [] 
    for i in range (k):
        centres.append(np.random.randint(0, X.shape[0]))
    print (centres)



if __name__ =="__main__":

    X,y = exo1.Data()
    initialize_centers(X,3)

