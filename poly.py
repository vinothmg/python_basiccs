"""
class animal():
    def sound(self):
        print("Animal Makes A Sound")
        
class dog(animal):
    def sound(self):
        print("Dog Barks")        
        
x1=dog()
x1.sound() 
"""

class person():
    def __init__(self,name):
        self.name=name
        
class student(person):
    def __init__ (self,name,grade):
        super(). __init__(name)
        self.grade=grade
        
    def display (self):
        print("Name  :", self.name)
        print("Grade :", self.grade)


x1=student("Ram", "A")        
x1.display()       