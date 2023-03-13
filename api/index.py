from flask import Flask, render_template, make_response
from flask_sitemap import Sitemap

app = Flask(__name__)
sitemap = Sitemap(app=app)

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

@app.route('/sitemap.xml', methods=['GET'])
def render_sitemap_xml():
    # Generate the sitemap dynamically
    sitemap_xml = render_template('sitemap.xml')
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"

    return response
