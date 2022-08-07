# Integrate HTML with Flask
# HTTP verb GET and POST

# jinja2 template engine

'''
{%...%} for statements
{{ }} expressions to print out
{#....#} this is for comments
'''

from pydoc import render_doc
from urllib import request
from flask import Flask,redirect,url_for,render_template,request

# WSGI application it is used to communicate between the web server and web application
app = Flask(__name__)

@app.route('/')  # decorator
def welcome():
    return render_template('index.html')

@app.route('/me')  # decorator
def members():
    return 'Welcome to my Youtube Channel guys'

# Building URLs dynamically and Variables rules & URL building
# own parameter value data type
@app.route('/success/<int:score>')
def success(score):
    # res = ''
    # if score >= 50:
    #     res = "PASS"
    # else:
    #     res = 'FALSE'

    # 3rd dictionary
    res = ''
    if score >= 50:
        res = 'PASS'
    else:
        res = 'FAIL'
    exp = {'score' :score,'res' : res}
    return render_template('result.html',result = exp)#res #score

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has passed and the marks is" + str(score)

# result checker
@app.route('/result/<int:marks>')
def results(marks):
    result = ''
    if marks > 50:
        result = 'fail'
    else:
        result = 'success'
    # it returns a response object and redirects the user to another target location with specified status code
    # url_for() function is used to build a URL to the specific function dynamically
    return redirect(url_for(result,score = marks))

# Result checker submit HTML page
@app.route('/submit',methods = ['POST','GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science =float(request.form['science'])
        maths =float(request.form['maths'])
        c =float(request.form['c'])
        data_science =float(request.form['datascience'])
        total_score = (science+maths+c+data_science)/4
    res= ''
    return redirect(url_for('success',score =total_score))


if __name__ == '__main__':
    app.run(debug = True)
