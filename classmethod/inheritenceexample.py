class Manish:
    def __init__(self):
        self.name = "manish"
        self.email = "manishverma88180@gmail.com"

    def bark(self):
        print("manish  is barkig ")


class SecondManish(Manish):
    def __init__(self):
        self.profile = "full stack"

    def mansig(self):
        print("this is the second maish")


secondmais = SecondManish()
print(secondmais.bark())
