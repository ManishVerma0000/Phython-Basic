class Manish:

    def __init__(self):
        self.name = "manish"
        self.occu = "develoer"

    def __add__(self, value1, value2):
        print(value1+value2)
        return value1+value2


class Manish2:
    def __init__(self):
        self.name = "verma"
        self.occu = "developer"


output1 = Manish().name
output2 = Manish2().name

Manish().__add__(output1, output2)
