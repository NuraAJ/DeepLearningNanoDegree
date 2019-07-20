import numpy as np


# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.

def cross_entropy(Y, P):
    cross_entropy_result = 0
    for y, p in zip(Y, P):
        cross_entropy_result += ((y * np.log(p)) + (1 - y) * np.log(1 - p))
    cross_entropy_result *= -1
    return cross_entropy_result


#model solution by Udacity
# import numpy as np
#
# def cross_entropy(Y, P):
#     Y = np.float_(Y)
#     P = np.float_(P)
#     return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))
