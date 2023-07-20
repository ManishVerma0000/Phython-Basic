class Manish:
    def __init__(self):
        print("inside the classone method")
        return

    def function1(self):
        print("inside the function one")
        return


class Second(Manish):
    def __init__(self):
        print("inside the second class constructor")
        return

    def function2(self):
        print("inside the seconnd class main function")
        return


class three(Second):
    def __init__(self):
        print("inside the third class constructor")

    def third(self):
        print("third function is here")
        return


thirdva = three()
print(thirdva.function2())

print(thirdva.function1())

print(thirdva.third())
