from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts = response.json()
print(all_posts)

@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html", all_posts=all_posts, current_year=current_year)

@app.route('/post/<int:id>')
def get_blog(id):
    return render_template("blog.html", all_posts=all_posts, id_number=id)

if __name__ == "__main__":
    app.run(debug=True)
