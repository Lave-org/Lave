from flask import Flask, render_template, request, redirect, url_for
from app.controller.main import Database

app = Flask(__name__, template_folder='app/views')



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/Houses')
def houses():
    return render_template('house.html')




@app.route('/Lands')
def lands():
    return render_template('lands.html')




@app.route('/Rents')
def rents():
    return render_template('rents.html')



@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/Login')
def login():

    return render_template('login.html')


@app.route('/Signup')
def signup():

    return render_template('signup.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    username = request.form.get('username')
    password = request.form.get('password')

    # Use the query_user method from Database class
    user = Database.query_user(username, password)

    if user:
        return redirect(url_for('success'))
    else:
        return redirect(url_for('failure'))

@app.route('/success')
def success():
    return "Login successful!"

@app.route('/failure')
def failure():
    return "Login failed. Please check your username and password. "

if __name__ == '__main__':
    app.run(debug=True)