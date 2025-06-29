import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (change host, user, and password if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # Replace with your actual MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Uncomment this line if you want to confirm connection close
            # print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
