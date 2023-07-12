integerone = input("enter the number first")
integersecond = input("enter the second number")
integerthree = input("enter the number third")


if (int(integerone) > int(integersecond) and int(integerone) > int(integerthree)):
    print("number one is largest", integerone)
elif (int(integersecond) > int(integerone) and int(integersecond) > int(integerthree)):
    print("second number is the largest number", integersecond)

else:
    print("the third number is the largest")
