import mysql.connector
from collections import defaultdict
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

 
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',         
        user='root',     
        password='Vkran@1234', 
        database='newdb'          
    )
    return connection

class RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path == '/api/orders':
            self.send_response(200)  
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            orders = self.fetch_orders()
            self.wfile.write(json.dumps(orders).encode())

        else:
            self.send_response(404)  
            self.end_headers()
            self.wfile.write(b'{"error": "Not Found"}')

    def fetch_orders(self):
        connection = get_db_connection()
        if connection is None:
            return {"error": "Could not connect to database"}

        cursor = connection.cursor(dictionary=True)

        
        cursor.execute('''
         select 
            o.order_id,
            o.sale_id,
            o.client_id,
            c.client_name,
            o.city AS order_city,
            c.city AS client_city,
            o.amount
        from 
            Orders o
        left join 
            Clients c ON o.client_id = c.client_id
            
           
    ''')
        results = cursor.fetchall()
        
        clients_dict=defaultdict(lambda: {
            'client_id':None,
            'client_name':None,
            'client_city':None,
            'orders':[] 
        })
        
     
    
        
        for row in results: 
            print("Processing row:", row)
            client_id = row['client_id']
        
        if client_id is not None:  
            if  clients_dict[client_id]['client_id'] is None:
                clients_dict[client_id]['client_id'] = client_id
                clients_dict[client_id]['client_name'] = row['client_name']
                clients_dict[client_id]['client_city'] = row['client_city']

            if row['order_id'] is not None:
                clients_dict[client_id]['orders'].append({
                    'order_id': row['order_id'],
                    'sale_id': row['sale_id'],
                    'order_city': row['order_city'],
                    'amount': row['amount']
                })

        cursor.close()
        connection.close()

  
def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8000)  
    httpd = server_class(server_address, handler_class)
    print('Starting server...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
    

