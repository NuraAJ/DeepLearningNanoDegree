import numpy as np


# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    result = []
    temp = 0
    sum = 0
    for l in L:
        sum += np.exp(l)
    for l in L:
        temp = np.exp(l) / sum
        result.append(temp)

    return result

# model solution from Udacity
# import numpy as np

# def softmax(L):
#     expL = np.exp(L)
#     sumExpL = sum(expL)
#     result = []
#     for i in expL:
#         result.append(i*1.0/sumExpL)
#     return result

#     # Note: The function np.divide can also be used here, as follows:
#     # def softmax(L):
#     #     expL = np.exp(L)
#     #     return np.divide (expL, expL.sum())
