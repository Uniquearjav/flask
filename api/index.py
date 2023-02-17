from flask import Flask , render_template

app = Flask(__name__)
def home():
    with open('header.html') as f:
        header_content = f.read()
    return render_template('index.html', header_content=header_content)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/footer")
def footer():
    with open('footer.html') as f:
        content = f.read()
    return content

@app.route('/header')
def header():
    with open('header.html') as f:
        content = f.read()
    return content

@app.route("/products")
def about():
    return render_template("product.html")