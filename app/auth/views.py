from flask import render_template,redirect,url_for,flash, request
from . import auth
from .forms import RegistrationForm,LoginForm
from .. import db
from ..models import Blogger
from flask_login import login_user,logout_user,login_required, current_user
from ..email import mail_message

@auth.route('/login',methods=['GET','POST'])
def login():
    '''
    function to log in the blogger
    '''
    login_form = LoginForm()
    if login_form.validate_on_submit():
        blogger = Blogger.query.filter_by(email = login_form.email.data).first()
        if blogger is not None and blogger.verify_password(login_form.password.data):
            login_user(blogger,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "My Blog Login"
    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/logout')
@login_required
def logout():
    '''
    function to log out the blogger
    '''
    logout_user()
    return redirect(url_for("main.index"))

@auth.route('/register',methods = ["GET","POST"])
def register():
    '''
    function to register or sign up a new blogger
    '''
    form = RegistrationForm()
    if form.validate_on_submit():
        blogger = Blogger(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(blogger)
        db.session.commit()

        mail_message("Welcome to My blog","email/welcome_user",blogger.email,blogger=blogger)

        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/signup.html',registration_form = form)