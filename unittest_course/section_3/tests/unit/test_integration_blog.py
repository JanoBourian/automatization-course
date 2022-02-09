import json
from unittest import TestCase
from blog import Blog

class TestIntegrationBlog(TestCase):
    
    def test_create_blog_with_posts(self):
        blog = {
            "title": "Lorem",
            "author": "Ergo Ipsofacto Columbo Oreo",
            "posts": [
            {"title": "Hello", "content": "Matrix"},
            {"title": "Python", "content": "FastAPI"},]}
        
        b = Blog(**blog)
        self.assertEqual(b.title, blog["title"])
        self.assertEqual(b.author, blog["author"])
        self.assertEqual(len(b.posts), len(blog["posts"]))
    
    def test_blog_json_format(self): 
        blog = {
            "title": "Lorem",
            "author": "Ergo Ipsofacto Columbo Oreo",
            "posts": [
            {"title": "Hello", "content": "Matrix"},
            {"title": "Python", "content": "FastAPI"},]}
        b = Blog(**blog)
        self.assertDictEqual(blog, b.json())