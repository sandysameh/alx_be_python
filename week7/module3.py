class Animal:
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        print("animal sound")

class Dog(Animal):
     def make_sound(self):
        print("wof")



class Flyer:
    def fly(self):
        print("flying ")


class Swimmer:
    def swim(self):
        print("swimming")

class Duck(Flyer,Swimmer):
    pass