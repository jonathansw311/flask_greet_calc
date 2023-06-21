from flask import Flask, request
from operations import *

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

@app.route('/add')
def addi():
    a = request.args["a"]
    b = request.args["b"]
    c = add(a,b)
    return(f"your values of {a} plus {b} eqals {c}")
  
@app.route('/sub')
def subt():
    a = request.args["a"]
    b = request.args["b"]
    c = sub(a,b)
    return(f"your values of {a} less {b} eqals {c}")

@app.route('/mult')
def multi():
    a = request.args["a"]
    b = request.args["b"]
    c = mult(a,b)
    return(f"your values of {a} times {b} eqals {c}")

@app.route('/div')
def divi():
    a = request.args["a"]
    b = request.args["b"]
    c = div(a,b)
    return(f"your values of {a} divided {b} eqals {c}")
   
@app.route('/math/<type>')
def math(type): 
   a = request.args["a"]
   b = request.args["b"]
   functions = {
       "add" : add(a,b),
       "sub": sub(a,b),
       "mult": mult(a,b),
       "div": div(a,b)
   }

   c = functions.get(type)
   return f"when you {type} {a} and {b} you get {c}"
   

