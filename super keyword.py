"""
class a():
    def __init__(self):
        print("A")
        
    def display(self):
        print("yor are in class A")
        
class b(a):
    def __init__(self):
         super().__init__()
         print("b")
    def display(self):
        print("you are in class B")  
        
class c(b,a):
    def __init__(self):
        super().__init__()
        print("c")
    def display(self):
        print("you are in class in C")               
         
         
x1=c()   
"""
"""
class person():
    def __init__(self,name):
        self.name=name 
        
        
class student(person):
    def __init__(self,name,grade):
        super(). __init__(name)
        self.grade=grade 
        
    def display(self):
        print(self.name,self.grade)
        
x1=student("John","A")
x1.display() 
"""

class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
class manager(employee):
    def __init__(self,name,salary,department):
        super(). __init__(name,salary)
        self.department=department  
        
    def display(self):
        print ("Name :", self.name)
        print ("Salary :", self.salary) 
        print ("Department :", self.department)    
        
x=manager("Raj", 25000, "Technical Support")
x.display()






     
                
        
                  
                         