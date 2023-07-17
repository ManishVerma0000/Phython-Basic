# # class Method:
# #     # Calling the __init__ method and initializing the attributes
# #     def __init__(self, attribute):
# #         self.attribute = attribute

# #     # Calling the __contains__ method
# #     def __contains__(self, attribute):
# #         return attribute in self.attribute


# # # Creating an instance of the class
# # instance = Method([4, 6, 8, 9, 1, 6])

# # # Checking if a value is present in the container attribute
# # print("4 is contained in ""attribute"": ", 4 in instance)
# # print("5 is contained in ""attribute"": ", 5 in instance)


# from typing import Any


# class addclass:
#     def __init__(self, x):
#         self.x = x

#     def __call__(self, numbergiven):
#         return self.x*numbergiven


# result = addclass(2)
# result(3)
# print(result(3))
# import wikipedia
# object = wikipedia.page("America")
# print(object.html)
n = 10
print(type(n))

new = "%s" % n
print(type(new))
