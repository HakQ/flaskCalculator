from app import app
from flask import Flask, request, render_template, session, redirect, url_for

@app.route('/', methods=['GET', 'POST'])
def index():
		if(request.method == 'GET'):
			return render_template("index.html")
		else:
			express = request.form.get('expression')
			expression = str(express)

			ac = expression.count('+')
			sc = expression.count('-')
			mc = expression.count('*')
			dc = expression.count('/')

			#check if the expression is valid
			if(sc == 1 and ac < 1 and mc < 1 and dc < 1):
				pos = expression.find('-')
				left, right = expression[:pos], expression[pos+1:]

				#check if the two operand are valid
				isNumb = left.isdigit() and right.isdigit()

    			#redirect to the subtract endpoint	
    			if(isNumb):
    				session['left'] = left
    				session['right'] = right
    				return redirect(url_for('subtract'))

			if (ac == 1 and sc < 1 and mc < 1 and dc < 1):
				pos = expression.find("+")
				left, right = expression[:pos], expression[pos+1:]
				
				#check if the two operand are valid
				isNumb = left.isdigit() and right.isdigit()

    			#redirect to the add endpoint	
    			if(isNumb):
    				session['left'] = left
    				session['right'] = right
    				return redirect(url_for('add'))

    		return "ERROR"
"""
			elif(expression.count('*') == 1 and expression.count('-') < 1 and expression.count('+') < 1 and expression.count('/') < 1):
				pos = expression.find('*')
				left, right = expression[:pos], expression[pos+1:]

			
				#check if the two operand are valid
				isNumb = left.isdigit() and right.isdigit()

    			#redirect to the multiply endpoint	
    			if(isNumb):
    				session['left'] = left
    				session['right'] = right
    				return redirect(url_for('multiply'))

			elif(expression.count('/') == 1 and expression.count('-') < 1 and expression.count('*') < 1 and expression.count('+') < 1):
				pos = expression.find('+')
				left, right = expression[:pos], expression[pos+1:]

				#check if the two operand are valid
				isNumb = left.isdigit() and right.isdigit()

    			#redirect to the divide endpoint	
    			if(isNumb):
    				session['left'] = left
    				session['right'] = right
    				return redirect(url_for('divide'))
			"""
			#return "BAD EXPRESSION!!!"


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