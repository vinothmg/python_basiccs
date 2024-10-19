import sqlite3
con=sqlite3.connect("C:\\Users\\admin\\OneDrive\\Desktop\\database.p\\database.db")

def insertData(name,age,city):
    qry="insert into users (NAME,AGE,CITY) values (?,?,?);"
    con.execute(qry,(name,age,city))
    con.commit()
    print("User Detials Added")
    
def updateData(name,age,city,id):
    qry="update users set NAME=?,AGE=?, CITY=? where  id=?;"
    con.execute(qry,(name,age,city,id))
    con.commit()
    print("User Detials updated") 
    
def deleteData(id):
    qry="delete from users where id=?;"
    con.execute(qry,(id))
    con.commit()
    print("User Detials deleted")   
    
def selectData():
    qry="select * from users"     
    result=con.execute(qry)
    for row in result:
        print(row)   

print("""
1.Insert
2.Update
3.Delete
4.Select
""")
ch=1
while ch==1:
    c=int(input("Select Your Choice"))
    if(c==1):
        print("Add New Record")
        name=input("Enter Name : ")
        age=input("Enter Age : ")
        city=input("Enter City : ")
        insertData(name,age,city)
    elif (c==2):
        print("Edit A Record")
        id=input("Enter Id : ") 
        name=input("Enter Name : ")
        age=input("Enter Age : ")
        city=input("Enter City : ")
        updateData(name,age,city,id)
    elif (c==3):
        print("Delete A Record")
        id=input("Enter Id : ") 
        deleteData(id)  
    elif (c==4):
        print("Print All Record")
        selectData()    
    else:
        print ("Invalid Selection")   
    ch=int(input("Enter 1 To Continue :"))  
        
 