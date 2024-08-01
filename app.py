from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'deepika1104'

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['pantry_tracker']

# Collections
users = db['users']
items = db['items']

# Create indexes for better performance (optional)
users.create_index('email', unique=True)
items.create_index('user_id')

@app.route('/')
def index():
    if 'user_id' in session:
        return render_template('index.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = users.find_one({'email': email})
        if user and check_password_hash(user['password'], password):
            session['user_id'] = str(user['_id'])
            return redirect(url_for('index'))
        flash('Invalid email or password')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        retype_password = request.form['retype_password']
        shop_name = request.form['shop_name']
        
        if password != retype_password:
            flash('Passwords do not match')
            return render_template('signup.html')

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        try:
            users.insert_one({
                'name': name,
                'email': email,
                'password': hashed_password,
                'shop_name': shop_name
            })
            return redirect(url_for('login'))
        except Exception as e:
            flash('Email already registered')
    return render_template('signup.html')

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        new_password = request.form['new_password']
        user = users.find_one({'email': email})
        if user:
            hashed_password = generate_password_hash(new_password, method='pbkdf2:sha256')
            users.update_one({'email': email}, {'$set': {'password': hashed_password}})
            flash('Password updated successfully. Please log in with your new password.')
            return redirect(url_for('login'))
        flash('Email not found')
    return render_template('forgot_password.html')

@app.route('/manage', methods=['GET', 'POST'])
def manage():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    if request.method == 'POST':
        item_name = request.form['item_name']
        item_quantity = request.form['item_quantity']
        items.insert_one({
            'user_id': ObjectId(user_id),
            'name': item_name,
            'quantity': item_quantity
        })
    
    user_items = list(items.find({'user_id': ObjectId(user_id)}))
    return render_template('manage.html', items=user_items)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
