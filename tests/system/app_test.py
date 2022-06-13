from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post

class AppTest(TestCase):
    
            
    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mi:
            app.menu()
            mi.assert_called_with(app.MENU_PROMPT)
            
    def test_menu_calls_print_blog(self):
        with patch('app.print_blogs') as mpb:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mpb.assert_called()
            
    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mi:
            mi.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')
            app.menu()
            self.assertIsNotNone(app.blogs['Test Create Blog'])
            
    def test_print_blog(self):
        b = Blog('Test', 'Test Author')
        app.blogs = {'Test':b}
        with patch('builtins.print') as mp:
            app.print_blogs()
            mp.assert_called_with('- Test by Test Author (0 posts).')
            
    def test_ask_create_blog(self):
        with patch('builtins.input') as mi:
            mi.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()
            
            self.assertIsNotNone(app.blogs.get('Test'))
            
            
    def test_ask_read_blog(self):
        b = Blog('Test', 'Test Author')
        app.blogs = {'Test':b}
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mpp:
                app.ask_read_blog()
                mpp.assert_called_with(b)
                
    def test_print_posts(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Author')
        app.blogs = {'Test':b}
        with patch('app.print_post') as mpp:
            app.print_posts(b)
            mpp.assert_called_with(b.posts[0])
    
    def test_print_post(self):
        post = Post('Post title','Post content')
        expected_print = app.POST_TEMPLATE.format('Post title', 'Post content')
        
        with patch('builtins.print') as mp:
            app.print_post(post)
            mp.assert_called_with(expected_print)
            
    def test_ask_create_post(self):
        b = Blog('Test', 'Test Author')
        app.blogs = {'Test':b}
        with patch('builtins.input') as mi:
            mi.side_effect = ('Test', 'Test Title', 'Test Content')
            
            app.ask_create_post()
            
            self.assertEqual(b.posts[0].title, 'Test Title')
            self.assertEqual(b.posts[0].content, 'Test Content')
        