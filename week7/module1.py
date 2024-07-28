class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person {self.name} has been created.")

    def __del__(self):
        print(f"Person {self.name} has been deleted.")

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

print("Deleting p1...")
del p1

print("p2 is still alive.")
