from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="homepage")

@app.route("/about")
def about():
    return render_template("about.html")

def plus(num1, num2):
    return num1 + num2 

if __name__ == "__main__":
    app.run(debug=True)

