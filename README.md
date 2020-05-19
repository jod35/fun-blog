# fun-blog
A blog app built with an intension of having fun with Python and the Flask Framework

## How it works
- Users sign up to get an account
- They then log in to their accounts
- Users can view blog posts and comment on posts.
- Users can delete and edit posts
- Admins can manage all user accounts

## Built with
- Flask
- Flask-Login 
- Flask-SQLAlchemy
- Flask-WTF
- Boostrap 4
- MySQL Database

## To run,
 - `git clone https://github.com/jod35/fun-blog.git`
 - `cd fun-blog`
 - `source venv/bin/activate`
 - `pip install -r requirements.txt`
 - `python3 app.py`
 
 ## To set up the database
 - `SQLALCHEMY_DATABASE_URI='mysql://<your_username>:<yourpassword>@localhost/<your_db>'
 - `export FLASKAPP=app.py` in the terminal
 - `flask db upgrade` in the terminal 

