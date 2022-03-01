# Main project file
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, template_folder="pages")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/donate")
def donate():
    return render_template("donate.html")
@app.route("/kwibuka")
def document():
    return render_template("kwibuka.html")

@app.route("/gallerywindow")
def gallerywindow():
    return render_template("gallerywindow.html")

if __name__ == "__main__":
    app.run(debug=False)