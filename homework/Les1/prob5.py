# too much text so have to type in eng sry
# have an english keyboard

profit = float(input("Please put income of your firm ($)\n>>>"))
costs = float(input("Put expenses of your firm ($)\n>>>"))

print("beep boop bob")
print("making calculations")
# used :.2f here to make it look official (was not sure if its ok in Pyth.)
if profit > costs:
    print(f"Congratulations You earning some cash, your rate is: {profit/ costs:.2f}")
    employee = int(input("How many people are working on you?\n>>>"))
    print(f"Profit per employee equals to: {profit/ employee:.2f} $")
else:
    print("Too bad your firm doesn't make any profit.")
