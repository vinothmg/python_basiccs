"""
try:
    
    print(a)
     
except NameError as e:
     print(" A is not Defined")
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
     
     