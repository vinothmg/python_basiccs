import mysql.connector
con=mysql.connector.connect(host='localhost', user='root', password='Vkran@1234', database='mydb')

def insert(id, name,age):
    res=con.cursor()
    sql="insert into users (id, name, age) values (%s,%s,%s)"
    user=(id,name,age)
    res.execute(sql,user)
    con.commit()
    print("Data Insert Sucess")

def update(id,name,age):
    res=con.cursor()
    sql="update users set name=%s, age=%s where id=%s"
    user=(name,age,id)
    res.execute(sql,user)
    con.commit()
    print("Data Update Sucess")

def select():
    res=con.cursor()
    sql="select id, name, age from users"
    res.execute(sql)
    result=res.fetchall()
    print(result)

def delete(id):
    res=con.cursor()
    sql="delete from users where id=%s"
    user=(id,)
    res.execute(sql,user)
    con.commit()
    print("Data Delete Sucess")


while True:
    
    print("1.insert data ")
    print("2.update data ")
    print("3.select data ")
    print("4.delete data ")
    print("5.exit ")
    
    
    choice=int(input("Enter Your Choice :"))
    
    if choice==1:
        id=input("Enter id :")
        name=input("Enter name :")
        age=input("Enter age :")
        insert(id,name,age)
        
    elif choice==2:
        id=input("Enter id :")
        name=input("Enter name :")
        age=input("Enter age :")
        update(id,name,age)
        
    elif choice==3:
        select()
        
    elif choice==4:
        id=input("Enter The id To Delete")
        delete(id)
        
    else:
        print("Invalid Selection")            
    