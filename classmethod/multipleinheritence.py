class School():
    def __init__(self):
        print("firs class")

    def multiplication(self, a, b):
        return a*b


class newschool():
    def __init__(self) -> None:
        pass

    def divided(self, a, b):
        return a % b


class lastclass(School, newschool):
    def __init__(self):
        print("inside the last school")


# resul = School().multiplication(2, 3)

# resultofdivided = newschool().divided(6, 3)
# print(resul)
# print(resultofdivided)


lastschoolresult = lastclass().multiplication(3, 4)
print(lastschoolresult)
