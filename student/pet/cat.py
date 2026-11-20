from pet.pet import Pet


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Meow"