from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import Blogger, Blog, Comments
from .forms import UpdateProfile,BlogForm, CommentForm
from .. import db
import markdown2

#views
@main.route('/')
@login_required
def index():
    '''
    view root page function that returns the index page and its data
    '''
    blog = Blog.get_blog()
    return render_template('index.html', blog=blog)

#adding a new blog
@main.route('/add/blog', methods=['GET', 'POST'])
@login_required
def nu_blog():
    '''
    function to insert or add new blog and fetch data from them
    '''
    form = BlogForm
    title = f'Welcome To Blogs'
    
    if form.validate_on_submit():
        content = form.content.data
        nu_blog = Blog(content=content, blog =blog.id,blog_id = current_user.id,)
        nu_blog.save_blogz()
        return redirect(url_for(',index', id=blog.id))
    return render_template('nu_blog.html', title= title,blog_form=form, blog = blog)

#viewing a pitch with it's comments
@main.route('/blog/view_blog/<int:id>', methods =['GET', 'POST'])
def view_blog(id):
    '''
    a function to view existing blogs
    '''
    print(id)
    blogz = Blog.get_blog(id)
    
    if blogz is None:
        abort(404)
        
    return render_template('blog.html',blogz=blogz)    
 
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/<uname>')
def profile(uname):
    '''
    a function to hold profile
    '''
    user = Blogger.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

#adding comments
@main.route('/new_comment/<int:id>', methods=['GET','POST'])
def new_comment(id):
    '''
    function that add comments
    '''
    form = CommentForm()
    comment = Comment.query.filter_by(pitch_id=id).all()
    blogs = Blog.query.filter_by(id=id).first()
    user = Blogger.query.filter_by(id = id).first()
    title=f'welcome to blogs comments'
        
    if form.validate_on_submit():
        feedback = form.comment.data
        new_comment= Comment(feedback=feedback,user_id=current_user.id,blog_id=blogs.id)
         
        new_comment.save_comment()
        return redirect(url_for('.index',uname=current_user.username))
    return render_template('comment.html', title = title, comment_form = form,blogs=blogs)
