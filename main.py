from flask import Flask, render_template
import requests

BLOG_POSTS_API = "https://api.npoint.io/43644ec4f0013682fc0d"

app = Flask(__name__)

response = requests.get(url=BLOG_POSTS_API)
json_data = response.json()

@app.route('/')
def home():
    return render_template("index.html", blog_posts=json_data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:ix>")
def show_post(ix):
    selected_post = None
    for blog_post in json_data:
        if blog_post["id"] == ix:
            selected_post = blog_post
            break
    return render_template("post.html", post=selected_post)


if __name__ == "__main__":
    app.run(debug=True)