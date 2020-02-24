from . import app,db
from flask import render_template,request,redirect,url_for,flash
from werkzeug.security import generate_password_hash,check_password_hash
from .forms import SignUpForm,LoginForm
from flask_login import login_user,logout_user,current_user,login_required
from .models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup',methods=['GET', 'POST'])
def sign_up():
    
    form=SignUpForm()
    if request.method == 'POST':
        username=form.username.data
        email=form.email.data
        password=form.password.data
        confirm=form.confirm.data
        user_exists=User.query.filter_by(username=username).first()
        email_taken=User.query.filter_by(email=email).first()

        if user_exists:
            flash("The username {} is already taken".format(username))
            return redirect(url_for('sign_up'))

        elif email_taken:
            flash("The email is already used")
            return redirect(url_for('sign_up'))

        elif password != confirm:
            flash("Passwords do not match!!")
            return redirect(url_for('sign_up'))
        else:
            new_user=User(
                username=username,
                email=email,
                password_hash=generate_password_hash(password)
            ) 
            db.session.add(new_user)
            password_hash=generate_password_hash(password)
            db.session.commit()
            flash("{}, creation of your account has been successful. You can now login.".format(username))
            return redirect(url_for('login'))
            
    context={   
        'form':form
    }
    return render_template('signup.html',**context)

@app.route('/login',methods=['GET', 'POST'])
def login():
    
    form=LoginForm()
    prompt=request.form.get('prompt')
    password=request.form.get('password')

    email_exists=User.query.filter_by(email=prompt).first()
    username_exists=User.query.filter_by(username=prompt).first()

    user_exist=email_exists or username_exists

    if user_exist and generate_password_hash(user_exist.password_hash,password):
        login_user(user_exist)
        return redirect('home_page')

    context={
        'form':form
    }
    return render_template('login.html',**context)

@app.route('/home')
def home_page():
    return render_template('home.html')