import numpy as np
import sys
np.set_printoptions(precision=3)

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

# iris = np.genfromtxt("../iris.data", delimiter=',', dtype='object')
# print(iris)


# task 25 ================================================== #
# How to extract a particular column from 1D array of tuples #

# iris_1d = np.genfromtxt("../iris.data", delimiter=',', dtype=None, encoding=None)
#
# iris = np.array([i[-1] for i in iris_1d])
#
# print(iris)


# task 26 =============================================== #
# How to convert a 1d array of tuples to a 2d numpy array #

# iris_1d = np.genfromtxt("../iris.data", delimiter=',', dtype=None, encoding=None)
#
# iris_2d = np.array([i.tolist()[:-1] for i in iris_1d])
#
# print(iris_2d)


# task 27 ============================================================ #
# How to compute the mean, median, standard deviation of a numpy array #

# iris_1d = np.genfromtxt("../iris.data", delimiter=',', dtype=None, encoding=None)
#
# # iris_sepal_length = np.array([i[0] for i in iris_1d])
# iris_sepal_length = np.genfromtxt("../iris.data", delimiter=',', dtype='float', usecols=[0])
#
# print(iris_sepal_length.mean(), np.median(iris_sepal_length), iris_sepal_length.std())


# task 28 ============================================================= #
# How to normalize an array so the values range exactly between 0 and 1 #

# iris_sepal_length = np.genfromtxt("../iris.data", delimiter=',', dtype='float', usecols=[0])
#
# print((iris_sepal_length - np.min(iris_sepal_length)) / iris_sepal_length.ptp())    # Max-Min Scaler


# task 29 ======================== #
# How to compute the softmax score #

# iris_sepal_length = np.genfromtxt("../iris.data", delimiter=',', dtype='float', usecols=[0])
#
# exponent = np.exp(iris_sepal_length)
#
# print(exponent / np.sum(exponent))


# task 30 ========================================== #
# How to find the percentile scores of a numpy array #

iris_sepal_length = np.genfromtxt("../iris.data", delimiter=',', dtype='float', usecols=[0])

print(np.percentile(iris_sepal_length, q=[5, 95]))
