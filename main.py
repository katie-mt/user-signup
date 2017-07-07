from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

#route and handler of the original form
@app.route("/")
def index():
    return render_template('form.html')

@app.route("/", methods = ['POST'])
def validate_form():
    
    username1 = request.form['username1']
    verify_password1 = request.form['password']
    verify_password2 = request.form['verify_password']
    e_address = request.form['email_address']

    username_error = ''
    password_error1 = ''
    password_error2 = ''
    email_error = ''

    #validating length of username and ensures no spaces.  If spaces or length issue found, return username_error
    if len(username1) < 3 or len(username1) > 20 or ' ' in username1:
        username_error = 'Please enter a valid username between 3-20 characters with no spaces'

    #validating length of password and ensures no spaces.  If spaces or length issues found, return password_error
    elif len(verify_password1) <3 or len(verify_password1) > 20 or ' ' in verify_password1:
        password_error1 = 'Please enter a valid password between 3-20 characters with no spaces'
    
    #checks to see if the two password fields match.  If not, displays the second error message.
    elif verify_password1 != verify_password2:
        password_error2 = 'Passwords do not match.  Please re-enter your password'

    elif '@' not in e_address or '.' not in e_address or ' ' not in e_address:
        email_error = 'Please enter a valid email address'
    elif not username_error and not password_error1 and not password_error2 and not email_error:
        return render_template('welcome.html', username1=username1)
    else:
        return render_template('form.html', username_error=username_error, password_error1=password_error1, password_error2=password_error2, email_error=email_error)


#route and handler to the welcome screen
@app.route("/welcome", methods=['POST', 'GET'])
def welcome():
    return render_template('welcome.html', username1=username1)

app.run()



#reject form if user's form submission is not valid.  Reject it and re-render the form with error messages.  The following should trigger an error:
    #The user leaves any of the following fields empty: username, password, verify password.
    #Email field may be empty, if not empty must contain a single @ and a single ., no spaces and between 3-20 characters
    #Each feedback message should be next to the field that it refers to.
    #For the username and email fields, you should preserve what the user typed, so they don't have to retype it. But clear the password fields.
#If all the input is valid, then show the user a welcome page that uses the username input to display a welcome message of: "Welcome, [username]!"
#Use templates (one for the index/home page and one for the welcome page) to render the HTML for your web app.
