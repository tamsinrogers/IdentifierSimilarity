

class Dog:
    def __init__(self, name, height, weight) -> None:

        self.name = name
        self.height = height
        self.weight = weight

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name


def a_function(a, b, c):

    e = a - b
    d = 0

    if e < 0:
        return None
    else:
        for i in range(e):
            d += c

    return d
