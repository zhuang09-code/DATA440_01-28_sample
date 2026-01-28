import numpy as np
import os

PATH_DATA = 'data'

# This file should contain code related to working with the data
# and nothing else

def make_data(n: int = 100, low: int = 0, high: int = 25) -> np.array:
    '''
    Return an nx2 array of random integers between low and high (inclusive)
    '''
    return np.random.randint(low=low, high=high+1, size=(n,2))

