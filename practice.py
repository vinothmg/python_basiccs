 #Write a Python Program to print Prime Numbers between 100 and 200
"""
for num in range(100,200):
    if all(num%i !=0 for i in range (2,num)):
            print(num)
"""            
            
"""          
for num in range(100, 200):
    
    if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
        print(num)
 """ 
 
 #Write a Sort function to sort the elements in a list     
""" 
l=[80,60,87,97,21,31]
l.sort()
print(l)
"""


#Write a sorting function without using the list.sort function
"""
data_list=[10,15,69,75,22,39,21]
new_list=[]

while data_list:
    minimum=data_list[0]
    for x in data_list:
        if x > minimum:
            minimum=x
            
    new_list.append(minimum)
    data_list.remove (minimum)
    
print(new_list)
"""

# Write a Python program to print a list in reverse
"""
l1=[1,2,3,4,5,6,7]
l2=l1[::-1]
print(l2)
"""
#writa a program to store a seven fruits in a list enter by user
"""
def collect_fruits():
    fruits = []  
    
    for i in range(7):
        fruit = input(f"Enter the name of fruit {i+1}: ")
        fruits.append(fruit)
    
    
    print("\nThe list of fruits is:")
    print(fruits)
 
collect_fruits()
"""

#write a program to count the number of zeros in the following tuple
"""
a=(2,3,5,0,5,0)
    
x=a.count(0)

print("Numbers Of Zeros In The Tuple:", x)   
"""

# write a program to greet  all the persons name stored in a list l1 and which starts with s
#l1 = ["Ram", "Sachin", "Rahul", "Saran", "Sam"]
"""
l1 = ["Ram", "Sachin", "Rahul", "Saran", "Sam"]

for name in l1:
    if name.lower().startswith('s'):
        print(f"Hello, {name}!")
"""
#get a input for a and b and pass it to function called printrange() 
# let the function print numbers fron a to b
"""
def printrange(r1,r2):
    for i in range(r1,r2):
        print(i)

a=int(input("Enter A:"))
b=int(input("Enter B:"))

printrange(a,b)   
"""
# create a function called add(),sub(),mul(),div(), and get the input
#for a and b inside every function that print the result
"""
a=int(input("A:"))
b=int(input("B:"))
     
operation=input("add/sub/mul/div:")

if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="mul"):
    print(a*b)
elif(operation=="div"):
    print(a/b)
else:
    print("Invalid Index")                        
"""

#get a integer number from user and pass it to the function called findevenorodd()
#whether the function print the number is odd or even
"""
def find_even_or_odd(i):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")


user=int(input("Enter An Integer:"))
find_even_or_odd(user)
"""

#abstract base class
"""
from abc import ABC, abstractmethod

class bank:
    @abstractmethod
    def loan(self):pass
    
    @abstractmethod
    def credit(self):pass
    
    @abstractmethod
    def debit(self):pass
    
class hdfc(bank):
    def loan(self):
        print("We Can Provide 7.5% Interest  Lone")
    def credit(self):
        print("hdfc provide credit")
    def debit(self):
        print("hdfc provide debit")
        
o=hdfc()
o.loan()  
o.credit()   
o.debit()  
"""  
"""
s = input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print("UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])
"""

#Define a class named Rectangle which can be constructed by a length and width. 
# The Rectangle class has a method which can compute the area.
"""
class rectangle:
    def __init__ (self,l,w):
        self.length=l
        self.width=w
        
    def area(self):
        return self.length*self.width
        
o=rectangle(2,10)
print(o.area())
"""


#assert
"""
l1 = [2,4,6,8]
for i in l1:
    assert i%2==0
"""
"""    
class animal():
    def sound(self):
        print("Animal makes sound")
        
class dog(animal):
    def sound(self):
        print("Dog Barks")
        
x=dog()
x.sound()
"""
"""
i=3
fact=1
while(i>0):
    fact=fact*i
    i=i-1
print(fact)
"""

"""
class school():
    def __init__ (self,name):        
        self.name=name
        
        
        
class student(school):
    def __init__(self,name,grade):
        super(). __init__(name)
        
        self.grade=grade   

    def display(self):
        print(self.name,self.grade)
        
x=student("Ram",  "A")
x.display()
"""

#nested for loop
"""
for i in range (6):
    for j in range(i):
        print("*",end="")
    print("")    
    
print("________")


for i in range (5,0,-1):
    for j in range(i):
        print("*",end="")
        
    print("")   
    
print("_______")


for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="")
    print("")
"""    
                
 
for i in range (6):
    for j in range(i):
        print("*",end="")
    print("")    
    
    
    
    

            