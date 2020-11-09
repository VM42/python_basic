# straight up example from Методичка not sure if I had to use randint for forming my_list


my_list = [2, 42, 69, 14, 8, 8, 420]
print(f"Исходный список: {my_list}")
# didn't get how to use prev_el
new_list = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(f"Новый список: {new_list}")
