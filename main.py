from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body>
    <h1>Signup
    </h1>
        <form action= "user-signup" method = "post">
            <table>
                <tr>
                    <td>
                        <label>Username:</label>
                    </td>
                    <td>
                        <input name = "username" type "text"/>
                    </td> 
                </tr>
                <tr>
                    <td>
                        <label>Password:</label>
                    </td>
                    <td>
                        <input name = "user-password" type = "password"/>
                    <td>
                </tr>
                <tr>
                    <td>
                        <label>Verify Password:</label>
                    </td>
                    <td>
                        <input name = "verify-password" type = "password"/>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label>Email Address:</label>
                    </td>
                    <td>
                        <input name = user-email" type = "email"/>
                    </td>
                </tr>
            </table>
            <input type = "submit"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/user-signup", methods = ['POST'])
def username():
    username = request.form['first_name']
    return '<h1>Hello, ' + username + '</h1>'
app.run()