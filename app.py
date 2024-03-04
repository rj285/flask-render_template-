from flask import Flask,render_template 

#render_template  used to render the html page

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile/<username>')
def rohit(username):
    return render_template('profile.html',username=username)

app.run(debug=True)

