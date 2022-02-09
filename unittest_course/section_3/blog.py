from post import Post 

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
    