class Dog:
    def make_sound(self):
        print("Wooof !")

class Bird:
    def make_sound(self):
        print("Flyyyyy !")

class Cat:
    def make_sound(self):
        print("Meowwwww !")

def let_them_speak(obj):
    obj.make_sound()

animals= [Cat(),Dog(),Bird()]

for animal in animals:
    let_them_speak(animal)

