

# Divided but not by zero

def my_div(arg_1, arg_2):

    try:
        result = arg_1 / arg_2
    except arg_1 == 0:
        return "Nah, you can't divide nothing"

    return print(result)


my_div(int(input("Enter your dividend\n>>>")), int(input("Enter your divider\n>>>")))
