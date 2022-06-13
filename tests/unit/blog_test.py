from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'TestAuthor')
        
        self.assertEqual('Test', b.title)
        self.assertEqual('TestAuthor', b.author)
        self.assertListEqual([], b.posts)
        
    def test_repr(self):
        b = Blog('Test', 'TestAuthor')
        b2 = Blog('By', 'ByBy')
        
        self.assertEqual(b.__repr__(), 'Test by TestAuthor (0 posts).') 
        self.assertEqual(b2.__repr__(), 'By by ByBy (0 posts).') 
        
    def test_repr_multiple_posts(self):
        b = Blog('Test', 'TestAuthor')
        b2 = Blog('Test', 'TestAuthor')
        b.posts = [1,2,3]
        b2.posts = [1,]
        
        self.assertEqual(b.__repr__(), 'Test by TestAuthor (3 posts).')
        self.assertEqual(b2.__repr__(), 'Test by TestAuthor (1 post).')