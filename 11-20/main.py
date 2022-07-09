import numpy as np


# task 11 ====================================================== #
# How to remove from one array those items that exist in another #

# a = np.array([1, 2, 3, 4, 5])
# b = np.array([5, 6, 7, 8, 9])
#
# print(np.setdiff1d(a, b))


# task 12 =================================================== #
# How to get the positions where elements of two arrays match #

# a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
# b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
#
# print(np.where(a == b)[0])


# task 13 =========================================================== #
# How to extract all numbers between a given range from a numpy array #

# a = np.array([2, 6, 1, 9, 10, 3, 27])
# print(a[(a >= 5) & (a <= 10)])


# task 14 ================================================================== #
# How to make a python function that handles scalars to work on numpy arrays #

# def max_x(x, y):
#     """Get the maximum of two items"""
#     if x >= y:
#         return x
#     else:
#         return y
#
#
# pair_max = np.vectorize(max_x, otypes=[float])
#
# a = np.array([5, 7, 9, 8, 6, 4, 5])
# b = np.array([6, 3, 4, 8, 9, 7, 1])
#
# print(pair_max(a, b))


# task 15 =================================== #
# How to swap two columns in a 2d numpy array #

# arr = np.arange(9).reshape(3, 3)
# print(arr)
# print(arr[:, [1, 0, 2]])


# task 16 ================================ #
# How to swap two rows in a 2d numpy array #

# arr = np.arange(9).reshape(3, 3)
# print(arr)
# print(arr[[1, 0, 2], :])


# task 17 ============================= #
# How to reverse the rows of a 2D array #

# arr = np.arange(9).reshape(3, 3)
#
# print(arr[::-1, :] == np.flip(arr, 0))


# task 18 ================================ #
# How to reverse the columns of a 2D array #

# arr = np.arange(9).reshape(3, 3)
#
# print(arr[:, ::-1] == np.flip(arr, 1))


# task 19 ========================================================== #
# How to create a 2D array containing random floats between 5 and 10 #

# print(np.random.uniform(5, 10, size=(5, 3)))


# task 20 ================================================ #
# How to print only 3 decimal places in python numpy array #

rand_arr = np.random.random((5, 3))
np.set_printoptions(precision=3)

print(rand_arr)



