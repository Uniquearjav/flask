from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def about():
    return render_template("products.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route('/sitemap.html')
def render_sitemap_html():
    return render_template("sitemap.html")

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml')
