from . import db
from  flask_migrate import Migrate, MigrateCommand
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return Blogger.query.get(int(user_id))

class Blogger(UserMixin,db.Model):
    '''
    Blogger class to define writter objects
    '''
    __tablename__ = 'blogger'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    password_secure = db.Column(db.String(255))
    blogz=db.relationship('Blog',backref= 'blogger',lazy='dynamic')
    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    
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
    posted = db.Column(db.DateTime, default =datetime.utcnow)
    blogger_id = db.Column(db.Integer, db.ForeignKey('blogger.id'))   
    comment = db.relationship ('Comments', backref ='blog')
                                      
    def save_blogz(self):
        '''
        function to save blogs
        '''
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def clear_bog(cls):
        Blog.all_blogs.clear()    
        
    def get_blog(id):
        blog = Blog.query.filter_by().all()
        return blog
    
    
class Comments(db.Model):
    '''
    class comment to define comments
    '''
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key = True)
    feedback = db.Column(db.String)
    blogger_id = db.Column(db.Integer, db.ForeignKey('blogger.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))    
    
    def save_comment(self):
        '''
        function to save comments
        '''
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_comments(self,id):
        '''
        function to get the comment
        '''
        comment = Comments.query.filter_by().all()
        return comment      
    
class Quote:
    '''
    class quote to define quote's Objects
    '''
    def __init__(self, id, author,quote):
        self.id = id
        self.author = author
        self.quote = quote 
        
class Subscribe(db.Model):
    __tablename__='subscribe'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    posted = db.Column(db.DateTime, default = datetime.utcnow)           
      