x = int(input("enter the number you want to print the star patter"))


for i in range(1, x):
    for j in range(i):
        print("*", end="")
    print("\r")
