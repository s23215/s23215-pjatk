#!/usr/bin/env python3

from flask import Flask, render_template, request, url_for, session

class User:
	def __init__(self, id, login, password):
		self.id=id
		self.login=login
		self.password=password
	def __repr__(self):
		return f'<User:{self.login}'
users=[]
users.append(User(id=1,login='Krystian', password='Banan'))


app = Flask(__name__)
app.secret_key="abc"

@app.route('/', methods=('GET', 'POST'))
def login():
	if request.method=='POST':
		login=request.form['login']
		password=request.form['pass']
		user=[x for x in users if x.login==login][0]
		if user and user.password==password:
			session['user_id']=user.id
			return render_template('index.html')
		else:
			return render_template('login.html', login=login, wrongpass='Wrong Password!')
	return render_template('login.html')



@app.route('/example', methods=('GET', 'POST'))
def example():
	lhs=int(request.form['firstnumber'])
	rhs=int(request.form['secoundnumber'])
	op=(request.form['sing'])
	result=0
	if (op=='+'):
		result=lhs+rhs
	elif (op=='-'):
		result=lhs-rhs
	elif (op=='*'):
		result=lhs*rhs
	elif (op=='/'and rhs!=0):
		result=lhs/rhs
	if (op=='/' and rhs==0):
		result="invaild"
	return str (result)

@app.route('/example2', methods=('GET', 'POST'))
def example2():
	return 'You said:{}'.format(request.form['firstname'])


