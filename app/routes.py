from app import app
from flask import Flask, request, render_template, session, redirect, url_for, jsonify
import json

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
    	arithmetic = request.form.get('arth')
    	left = request.form.get('num1')
    	right = request.form.get('num2')
    	try:
    		float(left)
    		float (right)
    	except ValueError:
    		return "You Entered some Bad Values!!!"
    	session['left'] = left
    	session['right'] = right
    	return redirect(url_for(arithmetic))
    elif request.method == 'GET':
        return render_template('index.html')

@app.route('/add')
def add():
	left = float(session.get('left', None))
	right = float(session.get('right', None))
	result = left + right
	return "Result: %s" % str(result)

@app.route('/subtract')
def subtract():
	left = float(session.get('left', None))
	right = float(session.get('right', None))
	result = left - right
	return "Result: %s" %str(result)

@app.route('/multiply')
def multiply():
	left = float(session.get('left', None))
	right = float(session.get('right', None))
	result = 0;

	#just incase number gets too big
	try:
		result = left * right
	except ValueError:
		return "BAD EXPRESSION!!"

	return "Result: %s" % result


@app.route('/divide')
def divide():
	left = float(session.get('left', None))
	right = float(session.get('right', None))
	result = 0;

	#just incase divide by 0
	try:
		result = left * right
	except ValueError:
		return "BAD EXPRESSION!!"

	return "Result: %s" % result
  
if __name__ == "__main__":
	app.debug = True
	app.run()