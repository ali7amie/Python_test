import numpy as np

def square_of_sum(count):
    table=np.arange(1,count+1)

    return (np.sum(table))**2


def sum_of_squares(count):
    table=np.arange(1,count+1)

    return np.sum(table**2)


def difference(count):

    return square_of_sum(count) - sum_of_squares(count)
