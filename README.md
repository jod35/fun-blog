# fun-blog
A blog app built with an intension of having fun with Python and the Flask Framework

# Built with
- Flask
- Flask-Login
- Flask-SQLAlchemy
- Flask-WTF
- Boostrap 4

# To run,
 - `git clone https://github.com/jod35/fun-blog.git`
 - `cd fun-blog`
 - `source venv/bin/activate`
 - `pip install -r requirements.txt`
 - `python3 app.py`
 
 # To set up the database
 - Change following in `simple_blog/config.py`
 `my_pw=<db_pw>`
 `SQLALCHEMY_DATABASE_URI='mysql://<db_user>:{}@localhost/simple'.format(my_pw)`
 where my_pw is your database user password
