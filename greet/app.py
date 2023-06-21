from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home_page():
    html="""<html>
    <body>
    <h1>Home</h1>
    <p>This is the "home" page</p>
    <a href='/hello'>Go to hello page</a>
    </body>
    </html>"""
    return html

@app.route('/welcome')
def welcome():
    return "Welcome"

@app.route('/welcome/home')
def welcomeHome():
    return "Welcome home"

@app.route('/welcome/back')
def welcomeBack():
    return "Welcome back"