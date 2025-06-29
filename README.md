# Discovering Databases: An Easy Start for Beginners
## Tasks 0
A Magical Database for Your Dream Online Bookstore Adventure!
mandatory
Imagine you’re tasked with designing a MySQL database for an online bookstore. The database should store information about books, authors, customers, orders, and order details. Here’s an overview of the database schema:

Database Name: alx_book_store

Books: Stores information about books available in the bookstore.

book_id (Primary Key)
title VARCHAR(130)
author_id (Foreign Key referencing Authors table)
price DOUBLE
publication_date DATE
Authors: Stores information about authors.

author_id (Primary Key)
author_name VARCHAR(215)
Customers: Stores information about customers.

customer_id (Primary Key)
customer_name VARCHAR(215)
email VARCHAR(215)
address TEXT
Orders: Stores information about orders placed by customers.

order_id (Primary Key)
customer_id (Foreign Key referencing Customers table)
order_date DATE
Order_Details: Stores information about the books included in each order.

orderdetailid (Primary Key)
order_id (Foreign Key referencing Orders table)
book_id (Foreign Key referencing Books table)
quantity DOUBLE
NOTE : - The file extension should be alx_book_store.sql file - All SQL keywords should be in uppercase

* Repo:

* GitHub repository: Intro_to_DB
* File: alx_book_store.sql
## Task 1. Let's Build Your Database: Your Gateway to Data Adventure!
mandatory
Write a simple python script that creates the database alx_book_store in your MySQL server.

Name of python script should be MySQLServer.py
If the database alx_book_store already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements
NOTE :

Required to print message such as Database 'alx_book_store' created successfully! when database is successfully created.

Print error message to handle errors when failing to connect to the DB.

handle open and close of the DB in your script.

* Repo:

* GitHub repository: Intro_to_DB
* File: MySQLServer.py
# Task 2. Create Your Magical Tables
mandatory
Write a script that creates all the tables below in alx_book_store in your MySQL server.

Tables

For each table/relation below, you can find the attributes in task 0
books
authors
customers
orders
order details
Name of the file should be task_2.sql

All SQL keywords should be in uppercase

* Repo:

* GitHub repository: Intro_to_DB
* File: task_2.sql
 
## Task 3. List all the tables created
mandatory
Write a script that list all the tables in alx_book_store in your MySQL server.

The name of the file should be task_3.sql
The database name will be passed as argument of mysql command
* Repo:

* GitHub repository: Intro_to_DB
* File: task_3.sql
## Task 4. Full description
mandatory
Write a script that prints the full description of the table books from the database alx_book_store in your MySQL server.

The database name will be passed as an argument of the mysql command
You are not allowed to use the DESCRIBE or EXPLAIN statements
The name of the file should be task_4.sql
All SQL keywords should be in uppercase
* Repo:

* GitHub repository: Intro_to_DB
* File: task_4.sql
## Task 5. Populating Your Database with Your Very First Data
mandatory
Write a script that inserts a single row in the table customer (database alx_book_store) in your MySQL server.

Singel data insertion

customer_id = 1
customer_name = Cole Baidoo
email = cbaidoo@sandtech.com
address = 123 Happiness Ave.
The database name will be passed as an argument of the mysql command

Name of the file should be task_5.sql

All SQL keywords should be in uppercase

* Repo:

* GitHub repository: Intro_to_DB
* File: task_5.sql
## Task 6. Populating Your Database with Your More Data
mandatory
Write a script that inserts multiple rows in the table customer (database alx_book_store) in your MySQL server.

Data insertion

    - `customer_id` = `2`
    - `customer_name` = `Blessing Malik`
    - `email` = `bmalik@sandtech.com`
    - `address` = `124 Happiness  Ave.`
    - `customer_id` = `3`
    - `customer_name` = `Obed Ehoneah`
    - `email` = `eobed@sandtech.com`
    - `address` = `125 Happiness  Ave.`
    - `customer_id` = `4`
    - `customer_name` = `Nehemial Kamolu`
    - `email` = `nkamolu@sandtech.com`
    - `address` = `126 Happiness  Ave.`
The database name will be passed as an argument of the mysql command

The name of the file should be task_6.sql

Well done on completing this project! Let the world hear about this milestone achieved.

🚀 Click here to tweet! 🚀

* Repo:

* GitHub repository: Intro_to_DB
* File: task_6.sql
