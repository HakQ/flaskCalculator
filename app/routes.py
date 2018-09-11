from app import app
from flask import Flask, request, render_template, session

@app.route('/', methods=['GET', 'POST'])
def index():
		if(request.method == 'GET'):
			return render_template("index.html")
		else:
			express = request.form.get('expression')
			expression = str(express)

			#check if the expression is valid
			if(expression.count('-') == 1 and expression.count('+') < 1 and expression.count('*') < 1 and expression.count('/') < 1):
				pos = expression.find("-")
				
				left, right = expression[:pos], expression[pos+1:]
				
				#check if the two operand are valid
				isNumb = left.isdigit() and right.isdigit()

    			#redirect to the add endpoint	
    			if(isNumb):
    				session['my_var'] = left
    				session['right'] = right
    				return redirect(url_for('add'))
    				
    			return "Invalid expression!!"

""" current point of debug

			elif(expression.count('+') == 1 and expression.count('-') < 1 and expression.count('*') < 1 and expression.count('/') < 1):
				pos = expression.find('+')
				left, right = expression[:pos], expression[pos+1:]

				#check if the two operand are valid
				isNumb = True
				try:
    				float(left)
    				float(right)
				except ValueError:
    				isNumb = False

    			#redirect to the subtract endpoint	
    			if(isNumb):
    				session['left'] = left
    				session['right'] = right
    				return redirect('/subtract')

			elif(expression.count('*') == 1 and expression.count('-') < 1 and expression.count('+') < 1 and expression.count('/') < 1):
				pos = expression.find('*')
				left, right = expression[:pos], expression[pos+1:]

				#check if the two operand are valid
				isNumb = True
				try:
    				float(left)
    				float(right)
				except ValueError:
    				isNumb = False

    			#redirect to the multiply endpoint	
    			if(isNumb):
    				session['left'] = left
    				session['right'] = right
    				return redirect('/multiply')

			elif(expression.count('/') == 1 and expression.count('-') < 1 and expression.count('*') < 1 and expression.count('+') < 1):
				pos = expression.find('+')
				left, right = expression[:pos], expression[pos+1:]

				#check if the two operand are valid
				isNumb = True
				try:
    				float(left)
    				float(right)
				except ValueError:
    				isNumb = False

    			#redirect to the divide endpoint	
    			if(isNumb):
    				session['left'] = left
    				session['right'] = right
    				return redirect('/divide')
			
			return "BAD EXPRESSION!!!"
"""

@app.route('/add')
def add():
	#left = float(session.get('left', none))
	#right = float(session.get('right', none))
	#result = left + right
	#return "Result: %s" % result
	return "SUCCESS"

@app.route('/subtract')
def subtract():
	left = float(session.get('left', none))
	right = float(session.get('right', none))
	result = left - right
	return "Result: %s" % result

@app.route('/multiply')
def multiply():
	left = float(session.get('left', none))
	right = float(session.get('right', none))
	result = 0;

	#just incase number gets too big
	try:
		result = left * right
	except ValueError:
		return "BAD EXPRESSION!!"

	return "Result: %s" % result


@app.route('/divide')
def divide():
	left = float(session.get('left', none))
	right = float(session.get('right', none))
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