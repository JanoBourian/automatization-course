from post import Post 
import os 
import sqlite3 

PATH = os.path.dirname(os.path.abspath(__file__))
DATABASE = "data.db"
FILE = PATH + "\\" + DATABASE

class Blog:
    def __init__(self, title: str, author: str, posts:list = None): 
        self.title = title
        self.author = author
        self.posts = [Post(**p) for p in posts] if posts else []

    def __repr__(self):
        return f"{self.title} by {self.author} with {len(self.posts)} posts"

    def create_post(self, title: str, content: str): 
        p = Post(title = title, content = content)
        self.posts.append(p)
        return p 
        
    def json(self):
        return {"title": self.title, "author": self.author, "posts": [post.json() for post in self.posts]} 
    
    @staticmethod
    def return_all_blogs():
        connection = sqlite3.connect(FILE)
        cursor = connection.cursor() 
        query = "SELECT * FROM blog;"
        result = cursor.execute(query)
        print(result)
        rows = result.fetchall() 
        if rows: 
            for row in rows: 
                query = "SELECT * FROM post WHERE blog = ?"
                print(row[0])
                print(query)
                result = cursor.execute(query, (row[0],))
                post = result.fetchall()
                print(post)
                
        connection.close()
        return [ {"title": r[1], "author": r[2]} for r in rows] if rows else None