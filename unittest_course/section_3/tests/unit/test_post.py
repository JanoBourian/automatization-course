from unittest import TestCase
from post import Post

class PostTestClass(TestCase):
    def test_create_post(self):
        title = 'Test'
        content = 'Test Content'
        p = Post(title, content)
        self.assertEqual(title, p.title) # OK
        self.assertEqual(content, p.content) # OK
        self.assertEqual("Hello", p.content) # FAIL