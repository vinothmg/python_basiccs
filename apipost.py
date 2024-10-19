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

   
    def do_POST(self):
        if self.path == '/api/users':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            user_data = json.loads(post_data)

            result = self.insert_user(user_data)

            self.send_response(201)   
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())

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

    def insert_user(self, user_data):
        connection = get_db_connection()
        if connection is None:
            return {"error": "Could not connect to database"}

        try:
            cursor = connection.cursor()
            sql = 'INSERT INTO users (name, city) VALUES (%s, %s)'
            cursor.execute(sql, (user_data['name'], user_data['city']))
            connection.commit()
            return {"id": cursor.lastrowid, "message": "User created successfully"}
        except mysql.connector.Error as err:
            return {"error": str(err)}
        finally:
            cursor.close()
            connection.close()


if __name__ == "__main__":
    run()
