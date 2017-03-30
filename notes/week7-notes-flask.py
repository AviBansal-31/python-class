# pip install flask
# root directory "webapp"
# new directory "app"
# in "app" new directory "static" and "templates"

# in "webapp" create run.py 
# in "app" create __init__.py and views.py

# in "__init__.py"
from flask inmport Flask
app = Flask(__name__)
from webapp.app import views

# in "run.py"
from webapp.app import app
app.run(debug= true)

# in "views.py"
from webapp.app import app
from flask import request, url_for, redirect, render_template
@app.route('/')
@app.route('/index')
def index():
  
  return "hello, world"
 
@app.route('/profile/username')
def profile(username):
  #return "hello,{}".format(username)
  return render_template(url_for,username = username)
# if 127.0.0.1:5000/profile/abc => print hello, abc

@app.route('/post/post_id')
def from_post(post_id):
  #return render_template(url_for)
  return "post id is {}".format(post_id)

@app.route('/projects/'.method=['GET','POST'])

def projects():
  return request.method
 
@app.route('/about') 
def about():
  return "this is an about page"

@app.route('/magic/username')
def magic(username):
  return redirect(url_for('profile', username=username))
  
