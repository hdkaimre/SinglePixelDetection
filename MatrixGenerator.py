__author__ = 'Hans Daniel Kaimre'

import numpy as np


def matrix_list(N,n): #N is number of matrices, n is the size of them
    mset=list() #creates a list, where we will insert the matrices
    for i in range(0,N-1):
        x=np.random.randint(2, size=(n, n))
        mset.append(x)
    return mset #returns the set
