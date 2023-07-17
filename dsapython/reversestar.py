
x = int(input("enter the number for the star pattern"))
for i in range(x, 1, -1):
    for j in range(i):
        print("*", end=" ")

    print("\r")
