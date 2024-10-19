 #Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
 
 #Create a Bus object that will inherit all of the variables and methods
 # of the parent Vehicle class and display it.
 
 #inherits from the Vehicle class. Give the capacity argument of Bus.
 # seating_capacity() a default value of 50.
 

class vehicle:
    def __init__(self, name, max_speed, milage):
        self.name=name
        self.max_speed=max_speed
        self.milage=milage
        
   
class bus(vehicle):
    def __init__(self,name,max_speed,milage,capacity=50):
         super(). __init__(name, max_speed, milage)
         self.capacity=capacity
         
    def seating_capacity (self):
          return f"The Seating Capacity Of{self.name} and {self.capacity} Capacity"
      
      
b1=bus("volvo", 160, 12)
print(b1.seating_capacity())         







    
         
      
           
        