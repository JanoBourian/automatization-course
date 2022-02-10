from unittest import TestCase
from unittest.mock import patch
from blog import Blog 
import app 

class TestApp(TestCase):
    
    def test_print_blogs(self): 
        blog = {
            "title": "Lorem",
            "author": "Ergo Ipsofacto Columbo Oreo",
            "posts": [
            {"title": "Hello", "content": "Matrix"},
            {"title": "Python", "content": "FastAPI"},]}
        
        b = Blog(**blog)
        app.blogs = {'TEST': b}
        with patch('builtins.print') as mocked_print: 
            app.print_blogs()
            mocked_print.assert_called_with(f"{b.title} by {b.author} with {len(b.posts)} posts")
            
    def test_menu_prints_prompt(self): 
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)
            
    def test_menu_calls_print_blogs(self): 
        with patch('app.print_blogs') as mocked_print_blogs: 
            with patch('builtins.input', return_value = '1'): 
                app.menu() 
                mocked_print_blogs.assert_called_with()