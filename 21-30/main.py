import numpy as np
import sys

# task 21 ============================================================================ #
# How to pretty print a numpy array by suppressing the scientific notation (like 1e10) #

# np.random.seed(100)
# rand_arr = np.random.random([3, 3]) / 1e3
# np.set_printoptions(suppress=True)
# print(rand_arr)


# task 22 ========================================================= #
# How to limit the number of items printed in output of numpy array #

# np.set_printoptions(threshold=6)
# print(np.arange(15))


# task 23 ============================================ #
# How to print the full numpy array without truncating #

# np.set_printoptions(threshold=6)
# a = np.arange(15)
# print(a)
# np.set_printoptions(threshold=sys.maxsize)
# print(a)


# task 24 ============================================================================== #
# How to import a dataset with numbers and texts keeping the text intact in python numpy #





