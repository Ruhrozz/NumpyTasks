import numpy as np


# task 31 ============================================ #
# How to insert values at random positions in an array #

# iris_2d = np.genfromtxt("../iris.data", delimiter=',', dtype='object')
#
# np.put(iris_2d, np.random.randint(iris_2d.size, size=20), np.nan)
#
# print(iris_2d)


# task 32 ================================================= #
# How to find the position of missing values in numpy array #

# iris_2d = np.genfromtxt("../iris.data", delimiter=',', dtype='float')
# iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan
#
# print(np.argwhere(np.isnan(iris_2d)))


# task 33 =================================================== #
# How to filter a numpy array based on two or more conditions #

# iris_2d = np.genfromtxt("../iris.data", delimiter=',', dtype='float', usecols=[0, 1, 2, 3])
#
# print(iris_2d[(iris_2d[:, 0] < 5) & (iris_2d[:, 2] > 1.5)])


# task 34 ======================================================== #
# How to drop rows that contain a missing value from a numpy array #

iris_2d = np.genfromtxt("../iris.data", delimiter=',', dtype='float', usecols=[0, 1, 2, 3])
np.put(iris_2d, np.random.randint(iris_2d.size, size=300), np.nan)

print(iris_2d[~np.any(np.isnan(iris_2d), axis=1)])
















