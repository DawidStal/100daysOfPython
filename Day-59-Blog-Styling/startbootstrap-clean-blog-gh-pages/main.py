from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
link = os.getenv("DAY59_LINK")
posts = requests.get(link).json()

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post')
def post():
    sample_post=posts[0]
    return render_template("post.html", post=sample_post)

@app.route('/post/<int:id>')
def post_id(id):
    for post in posts:
            if post["id"]==id:
                return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)