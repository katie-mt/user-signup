from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#tells where to look for the template

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)
#initialize the jinja templating engine using the template directory

app = Flask(__name__)
app.config['DEBUG'] = True

#route and handler of the original form
@app.route("/")
def index():
    template = jinja_env.get_template('form.html')
    return render_template(template)

@app.route("/", methods = ['POST'])
def validate_form():
    template = jinja_env.get_template('form.html')
    
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify password']
    email_address = request.form['email address']

    username_error = ''
    password_error = ''
    email_error = ''

    if request.method == 'POST':
        return welcome()

#route and handler to the welcome screen
@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    template = jinja_env.get_template('welcome.html')
    return render_template(template, username=username)

    #template = jinja_env.get_template('form.html')
    #return render_template('form.html', username=username)

app.run()



#reject form if user's form submission is not valid.  Reject it and re-render the form with error messages.  The following should trigger an error:
    #The user leaves any of the following fields empty: username, password, verify password.
    #The user's username or password is not valid -- it contains a space character or it consists of less than 3 characters or more than 20 
    #The user's password and password-confirmation do not match.
    #Email field may be empty, if not empty must contain a single @ and a single ., no spaces and between 3-20 characters
    #Each feedback message should be next to the field that it refers to.
    #For the username and email fields, you should preserve what the user typed, so they don't have to retype it. But clear the password fields.
#If all the input is valid, then show the user a welcome page that uses the username input to display a welcome message of: "Welcome, [username]!"
#Use templates (one for the index/home page and one for the welcome page) to render the HTML for your web app.



#global list for password
#password = []

#@app.route("/")
#def validate_password():
#    template = jinja_env.get_template('form.html')
#    return template.render(password=password)



#@app.route('/user-signup', methods=['POST'])
#def validate_form():
#    username = request.form['username']
#    password = request.form['password']
#    verify_password = request.form['verify password']
#    email_address = request.form['email address']

#    username_error = ''
#    password_error = ''
#    verify_password_error = ''
#    email_address_error = ''

#def validate_username(username):
#    if:
#    else:
    
#def validate_password(password):
#    if
#    else:

#@app.route('/user-signup', methods=['POST'])
#def validate_email(email):
#    if len(email) > 3:
#    and len(email) < 20:
#    #must code for contains . and contains @ here
#        return True
#    else:
#        return False


#@app.route("/user-signup", methods = ['POST'])
#def username():
#    username = request.form['first_name']
#    return '<h1>Hello, ' + username + '</h1>'

