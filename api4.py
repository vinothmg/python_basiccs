import socket
import mysql.connector
import json

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Vkran@1234',
        database='mydb'
    )
    
   
def handle_client_connection(users_socket):
    
    try:
        request_data = users_socket.recv(1024)  
        if not request_data:
            return
        
        data = json.loads(request_data.decode('utf-8'))
        id=data.get('id')
        name = data.get('name')
        age = data.get('age')

      
        if not id or name or not age:
            users_socket.sendall(b'Missing id or name or age\n')
            return

        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (id,  name, age) VALUES (%s, %s, %s)', (id, name, age))
        conn.commit()
        cursor.close()
        conn.close()

        users_socket.sendall(b'users added successfully\n')

    except mysql.connector.Error as err:
        users_socket.sendall(f'Database error: {err}\n'.encode())
    except json.JSONDecodeError:
        users_socket.sendall(b'Invalid JSON format\n')
    finally:
        users_socket.close() 
        
def start_server(host='localhost', port=8000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server_socket.bind((host,port))           
    server_socket.listen(5)
    
    print(f'server listening on {host}:{port}')
    
    while True:
        users_socket, addr = server_socket.accept() 
        print(f'Accepted connection from {addr}')
        handle_client_connection(users_socket) 

if __name__ == '__main__':
    start_server()
            