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

# iris_2d = np.genfromtxt("../iris.data", delimiter=',', dtype='float', usecols=[0, 1, 2, 3])
# np.put(iris_2d, np.random.randint(iris_2d.size, size=300), np.nan)
#
# print(iris_2d[~np.any(np.isnan(iris_2d), axis=1)])


# task 35 ======================================================== #
# How to find the correlation between two columns of a numpy array #

# iris_2d = np.genfromtxt("../iris.data", delimiter=',', dtype='float', usecols=[0, 1, 2, 3])
#
# print(np.corrcoef(iris_2d[:, 0], iris_2d[:, 2]))


# task 36 ======================================== #
# How to find if a given array has any null values #

# iris_2d = np.genfromtxt("../iris.data", delimiter=',', dtype='float', usecols=[0, 1, 2, 3])
#
# iris_2d[125, 1] = np.nan
#
# print(np.isnan(iris_2d).any())  # play with any's axis


# task 37 ================================================= #
# How to replace all missing values with 0 in a numpy array #

# iris_2d = np.genfromtxt("../iris.data", delimiter=',', dtype='float', usecols=[0, 1, 2, 3])
# iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan
#
# print(np.where(np.isnan(iris_2d), -1, iris_2d))
# # or
# # iris_2d[np.isnan(iris_2d)] = -1


# task 38 =============================================== #
# How to find the count of unique values in a numpy array #

# iris = np.genfromtxt("../iris.data", delimiter=',', dtype='object')
# names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
#
# for k, name in enumerate(names, 0):
#     print(name, np.unique(iris[:, k]).size)


# task 39 ============================================== #
# How to convert a numeric to a categorical (text) array #

# iris = np.genfromtxt("../iris.data", delimiter=',', dtype='object')
# names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
#
# handy = iris[:, 2].astype(float)
#
# iris[handy < 3, 2] = 'small'
# iris[handy >= 3, 2] = 'medium'
# iris[handy >= 5, 2] = 'large'
#
# print(iris)


# task 40 ========================================================= #
# How to create a new column from existing columns of a numpy array #

iris_2d = np.genfromtxt("../iris.data", delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')

column = (iris_2d[:, 2].astype(float) * np.pi * np.power(iris_2d[:, 0].astype(float), 2)) / 3

print(np.hstack((iris_2d, column.reshape(-1, 1))))



















