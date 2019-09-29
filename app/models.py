from . import db
from  flask_migrate import Migrate, MigrateCommand
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Blogger(UserMixin,db.Model):
    '''
    Blogger class to define writter objects
    '''
    __tablename__ = 'blogger'
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_secure = db.Column(db.String(255))
    blogz=db.relationship('Blog',backref= 'blogger',lazy='dynamic')
    # blog_id = db.Column(db.Integer, db,ForeignKey(blog.id))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'Blogger {self.username}'
    
class Blog(db.Model):
    '''
    Blog class to define blog objects
    '''
    __tablename__='blog'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    post = db.Column(db.String(255))
    posted = db.Column(db.datetime, default =datetime.utcnow)
    blogger_id = db.Column(db.Integer, db.ForeignKey('blogger_id')  
    
    def save_blogz(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def clear_bog(cls):
        Blog.all_blogs.clear()    
        
    def get_blog(cls):
        blog = Blog.query.filter_by().all_blogs
        return blog
    
    
class Comments(db.Model):
    '''
    class comment to define comments
    '''
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key = True)
    feedback = db.Column(db.String)
    blogger_id = db.Column(db.Integer, db.ForeignKey('blogger_id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blog_id'))    
    
    def save_comment(self):
        '''
        function to save comments
        '''
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_comments(self,id):
        comment = Comments.query.filter_by(blog_id = id).all()
        return comment        