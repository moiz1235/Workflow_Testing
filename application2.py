class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def graduate(self):
        if self.gpa > 3.0:
            return "Congrats on your graduation"
        else:
            return "Cannot graduate this semester"

    def writeSomething(self):
        with open('hello.txt', 'a+') as f:
            print("Hello World", file=f)
