from flask import Flask, render_template

app=Flask(__name__)


@app.route('/')
# The name of the function e.g. home() is the name that gets referred to in the href
# function in the html file
# e.g. <li><a href="{{ url_for("home") }}">Home</a></li>
def home():
    return render_template("home.html")
    # Need to have existing file ../templates/home.html
    # Needs to be in a 'templates' directory


@app.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
