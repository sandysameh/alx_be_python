class Bird:
    def fly(self):
        print("Flyinnggg")

class Mammal:
    def run(self):
        print("running")

class Bat(Bird,Mammal):
    pass

bat = Bat()
bat.fly()
bat.run()
