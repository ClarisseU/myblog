from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from . import db

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
   
#blog form    
class BlogForm(FlaskForm):
    content = TextAreaField('Post a blog', validators=[Required()])
    submit = submitField('submit Blog')  
    
#Comment Form
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Leave a comment')    