from flask import Flask,redirect,url_for

# WSGI application it is used to communicate between the web server and web application
app = Flask(__name__)

@app.route('/')  # decorator
def welcome():
    return 'Welcome to my Youtube Channel'

@app.route('/me')  # decorator
def members():
    return 'Welcome to my Youtube Channel guys'

# Building URLs dynamically and Variables rules & URL building
# own parameter value data type
@app.route('/success/<int:score>')
def fail(score):
    return "The person has failed and the marks is" + str(score)

@app.route('/fail/<int:score>')
def success(score):
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


if __name__ == '__main__':
    app.run(debug = True)
