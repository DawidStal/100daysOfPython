from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

blogs_url = "https://api.npoint.io/03229948056f685fe7d7"
blogs = requests.get(blogs_url).json()
posts = []
for blog in blogs:
    posts.append(Post(blog["id"],blog["title"],blog["subtitle"],blog["body"]))

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/post/<int:id>')
def view_post(id):
    for post in posts:
        if post.id==id:
            return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
