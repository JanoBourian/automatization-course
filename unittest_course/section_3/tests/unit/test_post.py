from unittest import TestCase
from post import Post

class PostTestClass(TestCase):
    def setUp(self):
        self.title = 'Test'
        self.content = 'Test Content'
        self.p = Post(self.title, self.content)
        
    def test_create_post(self):
        self.assertEqual(self.title, self.p.title) # OK
        self.assertEqual(self.content, self.p.content) # OK
        # self.assertEqual("Hello", p.content) # FAIL
    
    def test_post_json_format(self):
        expected = {"title": self.title, "content": self.content}
        self.assertDictEqual(expected, self.p.json()) # OK