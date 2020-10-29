# I confess, had to google how to work with // and % (modulo operator)
a = int(input("Put your number here\n>>>"))
m = a % 10
a = a//10
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a//10
print(f"Biggest digit in your number is: {m}")
