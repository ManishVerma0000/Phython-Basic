listofnumber = {
    "name": "manish",
    "class": "mtech ",
    "profile": "nodejsdeveloper"
}

# using enumerate function#
for index, items in enumerate(listofnumber):
    print(index)
    print(listofnumber[items])


count = 0
for items in range(1, 10):
    print(items)
    count = count+1
    print(count, 'this is the value of the count')
