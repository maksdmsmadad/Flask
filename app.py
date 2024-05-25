from flask import Flask, render_template
from flask_sqlalchemy import SQLALchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Flask.db'
db = SQLALchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=FAlse)
    text = db.Column(db.text, nullable=False)


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/defuse")
def defuse():
    return render_template('defuse.html')

@app.route("/volonter")
def volonter():
    return render_template('volonter.html')


if __name__ == '__main__':
    app.run(debug=True)
