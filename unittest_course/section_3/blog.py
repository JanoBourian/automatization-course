from post import Post 

class Blog:
    def __init__(self, title: str, author: str): 
        self.title = title
        self.author = author
        self.posts = []
    
    def create_post(self, title: str, content: str): 
        p = Post(title = title, content = content)
        self.posts.append(p)
        return p 
        
    
    def json(self):
        return {"title": self.title, "author": self.author, "posts": self.posts} 
    
    def __repr__(self):
        pass 