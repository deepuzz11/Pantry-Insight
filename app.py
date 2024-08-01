from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from config import MONGO_URI

app = Flask(__name__)
app.secret_key = 'supersecretkey'
client = MongoClient(MONGO_URI)
db = client.pantry

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db.users.insert_one({'email': email, 'password': password})
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = db.users.find_one({'email': email, 'password': password})
        if user:
            session['email'] = email
            return redirect(url_for('manage'))
    return render_template('login.html')

@app.route('/manage', methods=['GET', 'POST'])
def manage():
    if 'email' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        item_name = request.form['item_name']
        item_quantity = request.form['item_quantity']
        db.items.insert_one({'name': item_name, 'quantity': item_quantity, 'user': session['email']})
    
    items = db.items.find({'user': session['email']})
    return render_template('manage.html', items=items)

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
