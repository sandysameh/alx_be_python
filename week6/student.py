class student: 
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_student(self):
        print(f"Hi, My name is {self.name}. I am {self.age} years old")

newStudent = student("youssef","27")
print(newStudent.get_student())