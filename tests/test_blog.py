import unittest
from app.models import Blog,Blogger
from flask_login import current_user
from app import db

class TestBlog(unittest.TestCase):
    
    def setUp(self):
        self.blogger_me = Blogger(username = "Clarisse", password="123", email = "klaryc4@gmail.com")
        self.new_blog = Blog(title="live love laugh", post="nice")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog, Blog))
        
    def test_instance_variables(self):
        self.assertEquals(self.new_blog.post,'nice')   
        self.assertEquals(self.new_blog.title,'live love laugh') 
        
    def test_save_blog(self):
        self.new_blog.save_blogz()
        
    def test_get_blog(self):
        self.new_blog.save_blogz()
        blog = Blog.get_blog(111)         