import socket

def start_server(host='localhost', port=8000):
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
   
    server_socket.bind((host, port))
    
  
    server_socket.listen(5)
    print(f'Server listening on {host}:{port}')
    
   
    data = {
        'id':20,
        'name':'Jos',
        'city':'New York'
        }

    while True:
        try:
            
            client_socket, addr = server_socket.accept()
            print(f'Accepted connection from {addr}')
            
            
            request = client_socket.recv(1024)
            print(f'Received: {request.decode()}')
            
             
             
            client_socket.sendall(f'Client data received: {data}\n'.encode('utf-8'))
            
        except Exception as e:
            print(f'An error occurred: {e}')
        finally:
             
            client_socket.close()
if __name__ == '__main__':
    start_server()
