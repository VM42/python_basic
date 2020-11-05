
def my_sum_calc():
    result = 0
    numbers = input("Enter number or press ~ to exit:\n>>>").split(" ")
    for (i = 0, i < 42, i++):
        try:
            number = float(token)
            result += number
        except:
                if token == '~':
                    print(f"You sum is {result}. Thanks for using")
                    break
                else:
                    print(f"You sum is {result}.")
                    continue


my_sum_calc()
