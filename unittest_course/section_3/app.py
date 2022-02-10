from blog import Blog
import logging 
import sqlite3 
import os 

PATH = os.path.dirname(os.path.abspath(__file__))
DATABASE = "data.db"
FILE = PATH + "\\" + DATABASE

def menu(): 
    # Show the user the available blogs
    # Let the user make a choice 
    # Do something with that choice 
    # Eventually exit 
    
    res = print_blogs()
    print(res)

def print_blogs():
    return Blog.return_all_blogs()

def create_tables():
    connection = sqlite3.connect(FILE)
    cursor = connection.cursor() 
    create_table = "CREATE TABLE IF NOT EXISTS blog(\
        id INTEGER PRIMARY KEY, title text, author text)"
    cursor.execute(create_table)
    connection.commit() 
    create_table = "CREATE TABLE IF NOT EXISTS post(\
        id INTEGER PRIMARY KEY, title text, content text, blog INTEGER, \
        FOREIGN KEY (blog) REFERENCES blog(id))"
    cursor.execute(create_table)
    connection.commit() 
    connection.close()

def start(): 
    create_tables()
    menu() 

if __name__ == "__main__":
    start()