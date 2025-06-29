# Write a simple python script that creates the database alx_book_store in your MySQL server.

# Name of python script should be MySQLServer.py
# If the database alx_book_store already exists, your script should not fail
# You are not allowed to use the SELECT or SHOW statements
# NOTE :

# Required to print message such as Database 'alx_book_store' created successfully! when database is successfully created.

# Print error message to handle errors when failing to connect to the DB.

# handle open and close of the DB in your script.
import mysql.connector
from mysql.connector import errorcode
import config

# Database connection details (replace with your own)
def create_database():
    connection = None
    cursor = None

    try:

        connection  = mysql.connector.connect(
            host= config.host,
            user= config.user,
            password= config.password
        )

        mycursor = connection.cursor()

        # Creating database
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")


    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"Error: {err}")
    finally:
        # Close cursor and connection safely
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

# Function call
if __name__ == "__main__":
    create_database()