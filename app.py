
#no return type without argument function in python
"""
def add():
     a=int(input(" Enter The Value Of A : "))
     b=int(input(" Enter The Value Of B : "))
     c=a+b
     print(" Total", c)
add()   
"""

# no return with argument function
"""
def sub(a, b):
    c=a-b
    print("Difference:", c)
sub(25,2)    
"""

# return type without argument

"""
def mul():
     a=int(input(" Enter The Value Of A : "))
     b=int(input(" Enter The Value Of B : "))
     c=a*b
     return c
x=mul()
print("mul", x)    
"""
# return type with argument
"""
def div(a, b):
    c=a/b
    return c

x=div(25,2)
print("Division",x)  
"""
   
# keyword argument function
"""
def message(name, age):
    print(name, " age is", age)
    
message(age=25, name="ram")    
 """
 # default parameter function
"""
def user(name, city="Salem"):
     print(name, " is from ", city)
     
user("ram","chennai")
user("sam")    
 """
 
 #passinga list as an argument
"""
def  total(marks) :
     return sum(marks)
 
print ("Total :",total([20,40,70,80,90]))
 """
 
 #try block
"""      
try:
     a = 10/0
     a = 10/0
except Exception as e:
     print(e)                                      
     """ 

     
 
""" 
try:
     a = 10/25
     
except Exception as e:
     print(e)
else:
     print("A Value:",a)
"""

#name error exception
"""
try:
     print(a)
     
except NameError as e:
     print(" A is not Defined")   
 """
"""
try:
     print(10/0)
     
except ZeroDivisionError as e:
     print(" denominataor cant be zero ")     
"""

"""
try:
     a=int("ram")
     
except ValueError as e:
     print(" please enter numbers only ")  

 """
"""
try:
     a=[10,20,30,40]
     print(a[10])
except IndexError as e:
     print(" Invalid Index ")    
""" 
"""
try:
     f = open("test.txt") 
except FileNotFoundError:
     print("File Not Found")   
else:
     print(f.read())      
  """
  
"""
name1, name2, name3= input("Enter 3 Names:").split(',')
print ("Name 1:", name1)     
print ("Name 2:", name2)
print ("Name 3:", name3) 
"""
"""
n=int(input("Enter The Number:"))
if n % 2==0:
     print (n," is Even Number ")
 """
 # if else
"""
name=input("Enter Your Name:")
age=int(input("Enter Your Age:"))
if age>=18:
     print(name, "age is", age, "Eligibil for Vote")
else:
     print(name,"age is", age, "Not Eligible for Vote")      
 """
 
"""
days = int(input("Enter The Days:"))
if days == 0:
     print("Good No Fine")
     
elif days>=1 and days<=5:
     print("Fine Amount:", days * 0.5)
elif days>5 and days<=10:
     print("Fine Amount:", days * 1)
elif days>10 and days<=30:
     print("Fine Amount:", days * 5)
else:
     print("Membersip Cancle")                         
 """
"""
class student():
     name = "Ram Kumar"
     age = 25
     
 # getattr method
 
print(getattr(student, 'name'))
print(getattr(student,'age'))
print(getattr(student,'gender','no such attribute found'))
        
# dot notation
print(student.name)
print(student.age)      
""" 

#class method
"""
class student:
     name= "ram"
     age= 25
     
     def printall():
         print("name:", student.name)
         print("age:", student.age)
         
student.printall()         
print(student.__dict__)
"""
#instance method
"""
class student:
     name= "ram"
     age= 25
     
     def printall(self):
         print("name:", student.name)
         print("age:", student.age)
         
o=student()
o.printall()   
"""
# init method in python
"""
class user:
     def __init__(self, name):
          print("call  when  new instance created")
          self.name=name
           
     def printall(self):
         print("Name:", self.name)
          
          
o1 = user("Ram")
o1.printall()
print(o1.__dict__)
o2 = user("John")
o2.printall()
print(o2.__dict__)
print(user.__dict__)
""" 
"""
#property decorator

class user:
     def __init__(self, name, age) :
          self.name = name
          self.age = age
     
     #self.msg = self.name + " is " + str(self.age) + "Years Old"
     @property
     def msg(self):
          return  self.name + " is " + str(self.age) + " Years Old "
          
o = user("ram", 25)

print(o.name)
print(o.age)
print(o.msg)
o.age = 45
print(o.msg)
"""
#property decorater setter getter
"""
class student:
     def __init__(self, total) :
          self.total = total
          
     def average(self):
               return self.total / 5.0
          
o = student(450)
print("Total :",o.total)
print("Average :",o.average () )          
"""

#single inheritance
"""
class Nokia:
     company= "Nokia India"
     website= "www.nokia-in.com"
     
     def contact_details(self):
          print("Address: Cherry Road, Near Bus Stand, salem")
          
class Nokia1100(Nokia):
     def __init__(self):
          self.name = "Nokia 1100"
          self.year = 1998
     
     def product_details(self):
          print(" Name   : ", self.name)
          print("year    : ", self.year)
          print("company : ", self.company)
          print("website : ", self.website)
          
mobile = Nokia1100()
mobile.product_details()  
mobile.contact_details()  
"""

# method overriding
"""
class Employee:
     def WorkingHrs(self):
          self.hrs = 50
     def PrintHrs(self):
          print(" Total Working Hours:", self.hrs)
          
class Trainee(Employee):
     def WorkingHrs(self):
          self.hrs= 60
          
     def resetHrs(self):
          super().WorkingHrs()    


employee=Employee()
employee.WorkingHrs()
employee.PrintHrs()         

trainee=Trainee()
trainee.WorkingHrs()
trainee.PrintHrs()  

trainee.resetHrs()
trainee.PrintHrs()              

"""
#diamond problem
"""
class A:
     def display(self):
          print(" I am the display of A ")
          
class B(A):
     def display(self):
          print(" I am the display of class B")
   
class C(A):
     def display(self):
          print(" I am the display of class C")
           
class D(B,C):
      def display(self):
          print(" I am the display of class D") 
          
o = D()
o.display()
"""
#overloading
"""
class Addition:
     def __init__(self,a):
          self.a = a
          
     def __add__(o1,o2):
          return o1.a + o2.a 
     def __sub__(o1,o2):
          return o1.a - o2.a
          
          
          
o1 = Addition(10)
o2 = Addition(20)
 
print("Total:", (o1 + o2))  
print("difference:",(o1 - o2))        
"""

#abstract base class 
"""
from abc import ABC, abstractmethod

class Bank(ABC):
     @abstractmethod
     def loan(self):pass
     @abstractmethod
     def credit(self):pass 
     @abstractmethod
     def debit(self):pass
     
     
class HDFC(Bank):
     def loan(self):
          print("we can provind 7.5% Interest Loan")
     
     def credit(self):
          print("HDFC Provide Credit")
          
     def debit(self):
          print("HDFC Provide Debit")  
          
          
o=HDFC()
o.loan()
o.credit()
o.debit()                       
"""
       
"""
     
class student:
     def __init__(self, total):
          self._total= total  
     def average (self):
          return self._total / 5.0
     @property
     def total (self):
          return self._total
     @total.setter
     def total(self,t):
          self._total
          
     
o=student(450)
print("Total   :", o.total)
print("Average :", o.average())   
o.total=250  
print("Total   :", o.total)
print("Average :", o.average())    
"""

#arbitrary  keyword argument 
"""
def biodata(**data):
     print (data)
     
biodata ( name="Ram", age=25, gender="Male")         
"""
                      
     
#arbitrary argument
"""
def class_10 (*student):
     print(student)
     
class_10("Ram", "Sam", "Raj", "John")     
"""

#date time
"""
import datetime as dt

current_date=dt.date.today()
print("Current_date:", current_date)

new=dt.date(2021, 5, 22)
print(new)
print("year:",  new.year)
print("month:", new.month)
print("day:", new.day)

a=dt.time(10,45,12,2222)
print(a)
print("hour:", a.hour)
print("minute:", a.minute)
print("second:", a.second)
print("microsecond:", a.microsecond)        

current_time=dt.datetime.now()
print("Current_Time:", current_time )                

new=dt.datetime(2021, 5, 22, 10, 45, 12)
print(new)
print(new.date())
print(new.time())
"""

#name error exception
"""
try:
     print(a)
     
except NameError as e:
     print(" A is not Defined") 
     """
     
#zero division error
"""

     try:
     print(10/0)
     
except ZeroDivisionError as e:
     print(" Denominator Cant Be Zero") 
     """
"""     
try:
     a=int("Ram")
     
except ValueError as e:
     print(" Please Enter Number Only")  
     """
     
"""    
try:
     a=[20,30,40,50]
     print(a[6])
     
except IndexError as e:
     print(" Invalid Index")
     """ 

#multiple exception
"""

try:
     a=10/25
     print(a)
     
     b=[20,30,40,50]
     print(b[7])
     
except ZeroDivisionError:
     print("Denominator Cant Be Zero")     
except IndexError:
     print(" Invalid Index")
     """
     
"""    
m1=int(input(" Enter Mark-1:"))
m2=int(input(" Enter Mark-2: "))
m3=int(input(" Enter Mark-3: ")) 
total=m1+m2+m3
average=total/3.0
print("Total:", total)
print("average:", average)

if m1>=35 and m2>=35 and m3>=35:
     print("Result: Pass" )
     if average >=90 and average <=100:
          print("Grade: A")
     elif average >=80 and average <=89:
          print("Grade: B")
     elif average >= 70 and average <=79:
          print("Grade: C")
     else:
          print("Grade: D")
else:
     print("Result:Fail")  
     print("Grade: No Grade")                        
     """
     
#property decorator

"""
class user:
     def __init__(self, name, age):
          self.name= name
          self.age= age
        #  self.msg= self.name + "is" + str(self.age) + " Years Old "
        
     @property
     def msg(self):
          return self.name + "is" + str(self.age) + " Years Old "     
          
o=user("Ram", 25)
print(o.name)
print(o.age)
print(o.msg)
o.age= 45
print(o.msg)              
"""

"""
class student:
     def __init__(self, total) :
          self._total = total
          
     def average(self):
               return self._total / 5.0
     @property     
     def total(self):
          return self._total   
      
     @total.setter
     def total(self,t):
          if t<0 or t>500:
               print("Invalid Total Cant Change")
          self._total= t 
          
o = student(450)
print("Total :",o.total)
print("Average :",o.average ())  
o.total= 250
print("Total:", o.total)
print("Average:", o.average()) 
"""
 

 


#property method
"""
class student:
     def __init__(self, total) :
          self._total = total
          
     def average(self):
               return self._total / 5.0
         
     def getter(self):
          return self._total   
      
     
     def setter(self,t):
          if t<0 or t>500:
               print("Invalid Total Cant Change")
          self._total= t 
          
     total= property(getter, setter)     
          
o = student(450)
print("Total :",o.total)
print("Average :",o.average ())  
o.total= 250
print("Total:", o.total)
print("Average:", o.average())
"""

# Write a program which will find all such numbers which are divisible by 7 but 
# are not a multiple of 5, between 2000 and 3200 (both included). The numbers 
# obtained should be printed in a comma-separated sequence on a single line.

l=[]
for i in range(2000, 3200):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))




     
     
    
     


     
   

                  





       
          
     
 
 
 
 
 
 
 
 
 