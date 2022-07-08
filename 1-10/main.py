import numpy as np

# task 1 ================= #
# How to create a 1D array #

# print(np.arange(10))


# task 2 ====================== #
# How to create a boolean array #

# print(np.full((3, 3), True, dtype=bool))


# task 3 ========================================================== #
# How to extract items that satisfy a given condition from 1D array #

# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#
# print(arr[arr % 2 != 0])


# task 4 ======================================================================== #
# How to replace items that satisfy a condition with another value in numpy array #

# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#
# arr[arr % 2 != 0] = -1
#
# print(arr)


# task 5 =========================================================================== #
# How to replace items that satisfy a condition without affecting the original array #

# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#
# print(np.where(arr % 2 != 0, -1, arr))
# print(arr)


# task 6 ================ #
# How to reshape an array #

# arr = np.arange(10)
#
# print(arr.reshape(2, 5))
# print(arr.reshape(2, -1))
# print(np.reshape(arr, (2, 5)))


# task 7 =========================== #
# How to stack two arrays vertically #

# a = np.arange(10).reshape(2, -1)
# b = np.repeat(1, 10).reshape(2, -1)
#
# print(np.vstack((a, b)))


# task 8 ============================= #
# How to stack two arrays horizontally #

# a = np.arange(10).reshape(2, -1)
# b = np.repeat(1, 10).reshape(2, -1)
#
# print(np.hstack((a, b)))


# task 9 ===================================================== #
# How to generate custom sequences in numpy without hardcoding #

# a = np.array([1, 2, 3])    # to [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
#
# print(np.hstack((np.repeat(a, 3), np.tile(a, 3))))


# task 10 =================================================== #
# How to get the common items between two python numpy arrays #

a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

print(np.intersect1d(a, b))
