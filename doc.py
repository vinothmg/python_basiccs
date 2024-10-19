import mysql.connector

con=mysql.connector.connect( 
            host='localhost',
            user='root',
            password='Vkran@1234',  
            database='mydb'    )

def insert(id,name,age):
   res=con.cursor()
   sql="insert into users(id,name,age) values (%s, %s, %s)"
   user=(id,name,age)
   con.commit()
   print("Data Insert Sucess")
def update(id,name,age):
   res=con.cursor()
   sql="update users set name=%s, age=%s where id=%s"
   user=(name,age,id)
   res.execute(sql, user)
   con.commit()
   print("Data update Sucess")
def select():
    res=con.cursor()
    sql="SELECT ID,NAME,AGE from users"
    res.execute(sql)
    result=res.fetchall()
    print(result) 
    
def delete(id):
    res=con.cursor()
    sql="delete from users where id=%s"
    user=(id)
    res.execute(sql, user)
    con.commit()
    print("Data Deleted Sucessful")
    
while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")

    
    choice=int(input("Enter Your Choice : "))
    if choice == 1:
        id=input("Enter The Id :")
        name=input("Enter Name : ")
        age=input("Enter Age :")
        insert(id,name,age)
        
    elif choice == 2:
        id=input("Enter The Id : ")
        name=input("Enter Name : ")
        age=input("Enter Age :")
        update(name,age,id)
        
    elif choice ==3:
        select()
        
    elif choice ==4:
        id=input("Enter The Id To Delete : ")
        delete(id)
        
    elif choice ==5:
        quit()
        
    else:
        print("Invalid Selection . Please Try Again!")
    
    
    
    

        
        
        