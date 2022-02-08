from unittest import TestCase
from post import Post

class PostTestClass(TestCase):
    def test_create_post(self):
        title = 'Test'
        content = 'Test Content'
        p = Post(title, content)
        self.assertEqual(title, p.title) # OK
        self.assertEqual(content, p.content) # OK
        # self.assertEqual("Hello", p.content) # FAIL
    
    def test_post_json_format(self):
        title = 'Lorem'
        content = 'Lorem Content'
        p = Post(title, content)
        expected = {"title": title, "content": content}
        self.assertDictEqual(expected, p.json()) # OK