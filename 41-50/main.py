import numpy as np
import time


# task 41 ================================= #
# How to do probabilistic sampling in numpy #

# iris = np.genfromtxt("../iris.data", delimiter=',', dtype='object')
#
# names = [b'Iris-setosa', b'Iris-versicolor', b'Iris-virginica']
# p = [0.25, 0.25, 0.5]
#
# for i, k in zip(names, p):
#     specie = iris[iris[:, -1] == i]
#     print(specie[np.random.randint(0, specie.shape[0], round(specie.shape[0] * k))])


# task 42 ===================================================================== #
# How to get the second largest value of an array when grouped by another array #

# iris = np.genfromtxt("../iris.data", delimiter=',', dtype='object')
# names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
#
# sorted_petal_length = np.sort(iris[iris[:, -1] == b"Iris-setosa", 2]).astype(float)
#
# print(np.unique(sorted_petal_length)[-2])


# task 43 ========================== #
# How to sort a 2D array by a column #

# iris = np.genfromtxt("../iris.data", delimiter=',', dtype='object')
#
# print(iris[iris[:, 0].argsort()])


# task 44 =========================================== #
# How to find the most frequent value in a numpy array #

# iris = np.genfromtxt("../iris.data", delimiter=',', dtype='object')
#
# # Bad:
# # for i in np.unique(iris[:, 0]):
# #     print(i, np.count_nonzero(iris[:, 0] == i))
#
# # Good:
# vals, counts = np.unique(iris[:, 0], return_counts=True)
#
# print(np.vstack((vals, counts)).T)


# task 45 ============================================================================== #
# How to find the position of the first occurrence of a value greater than a given value #

# iris = np.genfromtxt("../iris.data", delimiter=',', dtype='object')
#
# print(np.argwhere(iris[:, 3].astype(float) > 1)[0])


# task 46 ============================================================== #
# How to replace all values greater than a given value to a given cutoff #

# a = np.random.uniform(1, 50, 20)
# # Bad:
# # a[a > 30] = 30
# # a[a < 10] = 10
# # Good:
# print(np.clip(a, 10, 30))


# task 47 =================================================== #
# How to get the positions of top n values from a numpy array #

# np.random.seed(100)
# a = np.random.uniform(1, 50, 20)
#
# n = 5
#
# print(np.argsort(a)[::-1][0:n])


# task 48 ============================================================= #
# How to compute the row wise counts of all possible values in an array #

# np.random.seed(100)
# arr = np.random.randint(1, 11, size=(60, 100))
#
# a = []
#
# for i in range(1, 11):
#     a.append(np.sum(arr == i, axis=1))
#
# print(np.array(a).T)


# task 49 ============================================== #
# How to convert an array of arrays into a flat 1d array #

# arr1 = np.arange(3)
# arr2 = np.arange(3, 7)
# arr3 = np.arange(7, 10)
#
# print(np.concatenate([arr1, arr2, arr3]))


# task 50 =============================================== #
# How to generate one-hot encodings for an array in numpy #

arr = np.random.randint(0, 4, size=6)

print(arr)

print((arr[:, None] == np.unique(arr)).astype(int))











