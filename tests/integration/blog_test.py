from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
        
    def test_create_post_in_blog(self):
        b = Blog('Test', 'TestAuthor')
        b.create_post('Test Post', 'TestContent')
        
        self.assertEqual(len(b.posts), 1)
        self.assertEqual('Test Post', b.posts[0].title)
        self.assertEqual('TestContent', b.posts[0].content)
        
        
    def test_json_with_post(self):
        b = Blog('Test', 'TestAuthor')
        b.create_post('Test Post', 'TestContent')
        expected = {
            'title': 'Test',
            'author': 'TestAuthor',
            'posts': [
                {
                    'title':'Test Post',
                    'content': 'TestContent',
                }
            ]
        }
        self.assertDictEqual(expected, b.json())
        
    def test_json_with_no_post(self):
        b = Blog('Test', 'TestAuthor')
        expected = {
            'title': 'Test',
            'author': 'TestAuthor',
            'posts': []
        }
        self.assertDictEqual(expected, b.json())
        
    def test_json_with_two_posts(self):
        b = Blog('Test', 'TestAuthor')
        b.create_post('Test Post', 'TestContent')
        b.create_post('Test Post1', 'TestContent1')
        expected = {
            'title': 'Test',
            'author': 'TestAuthor',
            'posts': [
                {
                    'title':'Test Post',
                    'content': 'TestContent',
                },
                {
                    'title':'Test Post1',
                    'content': 'TestContent1',
                }
            ]
        }
        self.assertDictEqual(expected, b.json())