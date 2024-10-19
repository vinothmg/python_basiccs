import mysql.connector
from mysql.connector import Error

# Function to create a connection to the database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Vkran@1234',  # Replace with your password
            database='mydb'    # Replace with your database name
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to close the database connection
def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Connection closed")

# Function to create a table
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                age INT 
            )
        """)
        connection.commit()
        print("Table created successfully")
    except Error as e:
        print(f"Error: {e}")

# Function to insert a new record
def create_record(connection, name, age):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
        connection.commit()
        print("Record inserted successfully")
    except Error as e:
        print(f"Error: {e}")

# Function to read records
def read_records(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        records = cursor.fetchall()
        for record in records:
            print(record)
    except Error as e:
        print(f"Error: {e}")

# Function to update a record
def update_record(connection, user_id, name, age):
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET name = %s, age = %s WHERE id = %s", (name, age, user_id))
        connection.commit()
        print("Record updated successfully")
    except Error as e:
        print(f"Error: {e}")

# Function to delete a record
def delete_record(connection, user_id):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        connection.commit()
        print("Record deleted successfully")
    except Error as e:
        print(f"Error: {e}")

# Main function to run the CRUD operations
def main():
    connection = create_connection()
    if connection:
        create_table(connection)
        create_record(connection, 'Alice', 30)
        create_record(connection, 'Bob', 25)
        print("Records after insertion:")
        read_records(connection)
        update_record(connection, 1, 'Alice', 31)
        print("Records after update:")
        read_records(connection)
        delete_record(connection, 2)
        print("Records after deletion:")
        read_records(connection)
        close_connection(connection)

if __name__ == "__main__":
    main()
