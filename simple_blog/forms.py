from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import StringField,PasswordField,SubmitField,SelectField

class SignUpForm(FlaskForm):
    username=StringField("Username",validators=[DataRequired("Please fill the field")])
    email=StringField("Email",validators=[DataRequired("Please fill the field."),Email("Must be an email")])
    password=PasswordField("Password",validators=[DataRequired("Please fill in the field"),EqualTo("confirm","Passwords do not match")]) 
    confirm=PasswordField("Confirm Password",validators=[DataRequired()])
    submit=SubmitField("SignUp")
class LoginForm(FlaskForm):
    prompt=StringField("Username or Email",validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired("Please fill in the field")]) 
    submit=SubmitField("Login")

