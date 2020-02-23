from . import app
from flask import render_template
from .forms import SignUpForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def sign_up():
    form=SignUpForm()
    context={
        'form':form
    }
    return render_template('signup.html',**context)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home_page():
    return render_template('home.html')