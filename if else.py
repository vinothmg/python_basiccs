"""
mehana=input()
if(mehana=="dead"):
    print("surya meets priya")
else:
    print("surya weds mehana")    
"""
"""
income=int(input())    
if(income>7000):
    print("Not Eligible For Scholership")

else:
    print("Eligible for scholership")        
"""    
#nested if
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
    print("Result : Fail")
    print("Grade : No Grade")
    """
    
"""

score=int(input("score:"))

if (score<35):
    print("Poor Student")
elif(score>=35 and score<70):
    print("Average Student") 
elif(score>=70 and score<=100):
    print("Good Student")
    
else:
    print("Invalid Score ")        
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
    print("Invalid Operation")        

       
    
   

        