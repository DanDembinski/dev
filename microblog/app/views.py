from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Dan'} #Fake user
	posts = [
		{
			'author': {'nickname' : 'John'},
			'body' : 'Beautiful Day out!'
		},
		{	'author': {'nickname': 'Dan'},
			'body' : 'Only four more days!'
		}
		]
	return  render_template('index.html',
				title='home',
				user=user,
				posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html',
				title='Sign In',
				form=form)
