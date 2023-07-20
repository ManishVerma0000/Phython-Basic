n = int(input("enter the number you want to print the star patter"))


# for i in range(1, x):
#     for j in range(i):
#         print("*", end="")
#     print("\r")

if (n % 2 != 0):
    print("Weird")
else:
    for i in range(2, 5):
        if (i == n):
            print("Not Weird")

    for i in range(6, 20):
        if (i == n):
            print("Weird")

    if (n > 20):
        print("Not Weird")
