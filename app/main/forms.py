from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
   
#blog form    
class BlogForm(FlaskForm):
    title = TextAreaField('title', validators=[Required()])
    post = TextAreaField('Post a blog', validators=[Required()])
    submit = SubmitField('submit Blog')  
    
#Comment Form
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Leave a comment')    
    
#subscribeForm
class SubscribeForm(FlaskForm):
    email = TextAreaField('subscribe', validators=[Required()])
    submit = SubmitField('submit')    