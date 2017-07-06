from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#tells where to look for the template

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))
#initialize the jinja templating engine using the template directory

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('form.html')
    return template.render()

#global list for username
username = []

@app.route("/")
def validate_username():
    template = jinja_env.get_template('form.html')
    return template.render(username=username)

#global list for password
password = []

@app.route("/")
def validate_password():
    template = jinja_env.get_template('form.html')
    return template.render(password=password)

app.run()

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


