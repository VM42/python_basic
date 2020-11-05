

# Divided but not by zero

def my_div(arg_1, arg_2):

    try:
        result = arg_1 / arg_2
    except ZeroDivisionError:
        return print("Nah, you can't  divide by nothing")

    return print(result)


my_div(int(input("Enter your dividend\n>>>")), int(input("Enter your divider\n>>>")))
