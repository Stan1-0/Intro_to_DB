import mysql.connector

def create_database():
    try:
        #opening a connection to db
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "StAvenue14875",
            database = "alx_book_store",
        )

        #creating the db
        cursor = mydb.cursor()
        sql = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        cursor.execute(sql)
        
        #close connection
        mydb.close()
        print("Database 'alx_book_store' created successfully!")
        
    except mysql.connector.Error as error:
        print(f"Failed to connect to MYSQL server or create database: {error}")
        
        