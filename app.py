#!/usr/bin/env python3

from flask import Flask, render_template, request

app = Flask(__name__)


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



@app.route('/')
def index():
	return render_template('index.html')
