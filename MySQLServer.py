import mysql.connector
from mysql.connector import errorcode
import config

# Database connection details (replace with your own)
def create_database():
    connection = None
    mycursor = None


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
        if mycursor:
            mycursor.close()
        if connection and connection.is_connected():
            connection.close()

# Function call
if __name__ == "__main__":
    create_database()