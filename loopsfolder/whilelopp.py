i = 1
arraya1 = []
arraya2 = []
while (i <= 100):
    if (i % 2 == 0):
        arraya1.append(i)
        print("the number is even", i)
    else:
        arraya2.append(i)
        print("the number is odd")
    i = i+1

print(arraya1, 'this is the list of the even number')
print(arraya2, 'this is the value of the odd number')


for item in range(len(arraya2)):
    print(item)

    if (item % 3 == 0):
        print("the given number is divided by three", item)
    else:
        print("the item is not divides by 3")
