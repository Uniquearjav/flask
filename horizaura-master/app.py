from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/header")
def header():
    return render_template("header.html")

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

    # add 404 when page not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
