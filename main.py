from flask import Flask, render_template, request, redirect, url_for
from train import make_prediction
from flask_sqlalchemy import SQLAlchemy
import time
import random

def check_if_codewords(inp):
    if Post.query.all() != None or Post.query.all() == False:
        posts = Post.query.all()
        for idx, post in enumerate(posts):
            if post.codewords == inp:
                return idx
    return -1

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    messages = db.Column(db.Text(),nullable=False)
    codewords = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f"Post('{self.messages}', '{self.codewords}')"

results = []
def update_results(initial, result):
    results.append([initial,result])
    return results

@app.route('/', methods=["POST","GET"])
def homepage():
    if request.method == "POST":
        prediction = request.form["prediction"]
        idx = check_if_codewords(prediction)
        if(idx != -1):
            all_posts = Post.query.all()
            results = update_results(prediction,all_posts[idx].messages)
            return render_template("index.html", length = len(results), results = results, codeword = False)
        else:
            result = make_prediction(prediction)
            results = update_results(prediction,result)
            return render_template("index.html", length = len(results), results = results, codeword = False)
    else:
        results = []
        return render_template("index.html", length = len(results), results = results, codeword = False)

@app.route("/post", methods=["POST", "GET"])
def mainfunc():
    if request.method=="POST":
        form = request.form
        messages = form["messages"]
        codewords = form["codewords"]
        post = Post(messages=messages, codewords=codewords)
        db.session.add(post)
        db.session.commit()
    return render_template("post.html")

@app.route("/past_msgs", methods=["POST", "GET"])
def past_posts():
    all_posts = Post.query.all()
    return render_template("past_msgs.html", posts = all_posts)

all_rants = []
def update_rants(rants, response):
    all_rants.append((rants,response))
    return all_rants

def get_response():
    possible = ['Ah okay', 'I see, how does that make you feel?', 'Hmmm', 'I understand, that musn\'t be nice', 'Ohhhh', 'I understand where you\'re coming from']
    return random.choice(possible)

@app.route("/rant", methods=["GET", "POST"])
def rant():
    if request.method == "POST":
        rant = request.form["rant"]
        rants = update_rants(rant,get_response())
        return render_template('rant.html', length = len(rants), rants=rants)
    else:
        all_rants = []
        return render_template('rant.html', length = len(all_rants), rants=all_rants)

@app.route("/resources",methods=["POST", "GET"])
def website():
    return render_template("resources.html")

@app.route("/hotlines", methods = ["POST", "GET"])
def hotlines():
    return render_template("hotlines.html")

@app.route("/about", methods = ["POST", "GET"])
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)





