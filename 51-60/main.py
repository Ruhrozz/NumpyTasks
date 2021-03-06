import numpy as np


# task 51 =================================================== #
# How to create row numbers grouped by a categorical variable #

# np.random.seed(100)
#
# species = np.genfromtxt("../iris.data", delimiter=',', dtype='str', usecols=[4])
# species_small = np.sort(np.random.choice(species, size=20))
#
# print([i for val in np.unique(species_small) for i, grp in enumerate(species_small[species_small == val])])
#
# booleans = species_small[:, None] == np.unique(species_small)
# print(np.cumsum(booleans, axis=0)[booleans] - 1)


# task 52 ===================================================== #
# How to create group ids based on a given categorical variable #

# np.random.seed(100)
#
# species = np.genfromtxt("../iris.data", delimiter=',', dtype='str', usecols=[4])
# species_small = np.sort(np.random.choice(species, size=20))
#
# print(np.argwhere(species_small[:, None] == np.unique(species_small))[:, 1])


# task 53 ================================= #
# How to rank items in an array using numpy #

# np.random.seed(10)
#
# a = np.random.randint(20, size=10)
# print(a.argsort().argsort())


# task 54 ================================================= #
# How to rank items in a multidimensional array using numpy #

# np.random.seed(10)
#
# a = np.random.randint(20, size=[2, 5])
# print(a)
# print(a.flatten().argsort().argsort().reshape(a.shape))


# task 55 ===================================================== #
# How to find the maximum value in each row of a numpy array 2d #

np.random.seed(100)
a = np.random.randint(1, 10, [5, 3])
print(a)










