from itertools import count
from itertools import cycle


# A func for counting from start to stop
def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)


# or
# def my_count_func_b(a):
#   for el in count(a):
#        if el in count > 10:
#            break
#        else:
#            print(el)


# B func
def my_cycle_func(my_list, iteration):
    i = 0
    repeats = cycle(my_list)
    while i < iteration:
        print(next(repeats))
        i += 1


my_count_func(int(input("Enter start number:\n>>> ")), int(input("Enter stop number:\n>>> ")))
my_cycle_func([4, 2, 0], int(input("Enter iteration:\n>>> ")))
# my_count_func_b(int(input("Enter start number:\n>>> ")))

