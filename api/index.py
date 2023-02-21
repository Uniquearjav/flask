from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def about():
    return render_template("product.html")

# Create a SQLite database and table to store login details
conn = sqlite3.connect('login.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT, password TEXT)''')
conn.commit()
conn.close()

# Endpoint for handling login requests
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the entered login details are valid
        conn = sqlite3.connect('login.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            # If the login details are valid, redirect to a success page
            return 'Login successful!'
        else:
            # If the login details are invalid, redirect to the login page with an error message
            return 'Invalid login details. Please try again.'
    else:
        return render_template('login.html')

# Endpoint for handling registration requests
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username is already taken
        conn = sqlite3.connect('login.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = c.fetchone()

        if existing_user:
            # If the username is already taken, redirect to the registration page with an error message
            return 'Username already taken. Please choose a different username.'
        else:
            # If the username is available, insert the registration details into the SQLite database
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()

            # Redirect the user to the login page
            return redirect(url_for('login'))
    else:
        return render_template('register.html')