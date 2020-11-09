# List and its multiplication

from functools import reduce


# that's some huge ny=umber
def my_func(prev_el, el):
    return prev_el * el


my_list = [el for el in range(100, 1000, 2)]


print(reduce(my_func, my_list))
