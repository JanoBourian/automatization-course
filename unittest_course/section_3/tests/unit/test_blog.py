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