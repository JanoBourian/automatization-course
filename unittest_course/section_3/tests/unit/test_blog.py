from unittest import TestCase
from blog import Blog 

class BlogTestClass(TestCase):
    def test_create_blog(self):
        title = "Blog random"
        author = "Django Rendhairt"
        b = Blog(title=title, author=author)
        self.assertEqual(title, b.title)
        self.assertEqual(author, b.author)
        self.assertListEqual([], b.posts)
        self.assertEqual(len([]), len(b.posts))
    
    def test_repr_method_with_zero_posts(self):
        title = "Blog random"
        author = "Django Rendhairt"
        b = Blog(title=title, author=author)
        self.assertEqual(b.__repr__(), f"{title} by {author} with {len(b.posts)} posts")
    
    def test_repr_method_with_some_posts(self):
        title = "Blog random"
        author = "Django Rendhairt"
        b = Blog(title=title, author=author)
        b.posts = ["One", "Two", "Three", "Four", "Five"]
        self.assertEqual(b.__repr__(), f"{title} by {author} with {len(b.posts)} posts")