

with open("some.txt", "w", encoding="UTF-8") as x_files:
    line = input("Enter something \n>>> ")
    while line:
        x_files.write(input("Anything else:\n>>> "))
        if not line:
            x_files.readlines()
            x_files.close()
            break
