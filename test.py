class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Pet: {self.name}\nAge: {self.age}")


kentaro = Pet('kentaro', 5)
kentaro.show()
