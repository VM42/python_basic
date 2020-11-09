# .count made it ez

my_list = [1, 1, 3, 3, 3, 5, 6, 4, 6, 2, 7, 7, 5, 0]
new_list = [el for el in my_list if my_list.count(el) < 2]
print(new_list)
