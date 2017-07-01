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

@app.route("/user-signup", methods = ['POST'])
def username():
    username = request.form['first_name']
    return '<h1>Hello, ' + username + '</h1>'
app.run()