"""
class laptop:
      def __init__(self,ram,processor):
        self.ram=ram
        self.processor=processor
      def display(self):
        print("ram :", self.ram)
        print("processor :", self.processor) 

hp=laptop(ram="8GB", processor="i5")
dell=laptop(ram="6gb", processor="i7")

hp.display()
dell.display()
"""

#can u create a vehicle class and include colour of the car,how old the car is
# and how many seats car has

class vehicle:
  def __init__ (self,colour,old,seats):
    self.colour=colour
    self.old=old
    self.seats=seats
    
  def display(self):
    print("Colour Of Car :", self.colour)
    print("Age Of Car    :", self.old)
    print("Seats In Car  :", self.seats)
    
x1=vehicle(colour="blue", old=13, seats=4)
x1.display()      

x2=vehicle(colour="white", old=5, seats=5)
x1.display()







