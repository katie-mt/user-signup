from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

#route and handler of the original form
@app.route("/")
def index():
    return render_template('form.html')

@app.route("/user_signup", methods = ['POST'])
def validate_form():
    username1 = request.form['username1']
    verify_password1 = request.form['verify_password1']
    verify_password2 = request.form['verify_password2']
    e_address = request.form['user-email']

    username_error = '' 
    password_error1 = ''
    password_error2 = '' 
    email_error = '' 

    #validating length of username and ensures no spaces.  If spaces or length issue found, return username_error
    if len(username1) < 3 or len(username1) > 20 or ' ' in username1:
        username_error = 'Please enter a valid username between 3-20 characters with no spaces'

    #validating length of password and ensures no spaces.  If spaces or length issues found, return password_error
    if len(verify_password1) <3 or len(verify_password1) > 20 or ' ' in verify_password1:
        password_error1 = 'Please enter a valid password between 3-20 characters with no spaces'
    
    #checks to see if the two password fields match.  If not, displays the second error message.
    if verify_password1 != verify_password2:
        password_error2 = 'Passwords do not match.  Please re-enter your password'

    if '@' not in e_address or '.' not in e_address or ' ' not in e_address:
        email_error = 'Please enter a valid email address'
    if username_error != "" or password_error1 != "" or password_error2 != "" or email_error != "":
        return render_template('/form.html', username_error=username_error, password_error1=password_error1, password_error2=password_error2, email_error=email_error)
    return render_template('welcome.html', username1=username1)


app.run()

