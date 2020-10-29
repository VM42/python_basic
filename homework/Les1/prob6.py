# funny but this one is quite ez

a = int(input("Введите результат в первый день (км)\n>>>"))
b = int(input("Введите желаемый результат (км)\n>>>"))
i = 1
while a < b:
    a *= 1.1
    i += 1
print(f"Дней: {i}")
