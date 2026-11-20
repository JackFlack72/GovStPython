from pet.pet import Pet


class Bird(Pet):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Tweet"