import mysql.connector
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

 
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',         
        user='root',     
        password='Vkran@1234', 
        database='mydb'          
    )
    return connection

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/api/users':
            self.send_response(200)  
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            users = self.fetch_users()
            self.wfile.write(json.dumps(users).encode())

        else:
            self.send_response(404)  
            self.end_headers()
            self.wfile.write(b'{"error": "Not Found"}')

    def fetch_users(self):
        connection = get_db_connection()
        if connection is None:
            return {"error": "Could not connect to database"}

        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        cursor.close()
        connection.close()

        return users

def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 5000)  
    httpd = server_class(server_address, handler_class)
    print('Starting server...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
    
 