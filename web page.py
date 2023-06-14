# ----------------------------------------
# -- Flask => Intro and Your First Page --
# ----------------------------------------
# - Flask Is Micro Framework Built With Python
# --------------------------------------------
# - HTML
# - CSS
# - JavaScript
# --------------------------------------------

from flask import Flask, render_template

skills_app = Flask(__name__)


@skills_app.route("/")
def homepage():
    return render_template('homepage.html')


@skills_app.route("/Signupforfree")
def sign():
    return render_template('Signupforfree.html')


@skills_app.route("/Getstarted")
def sign1():
    return render_template('Getstarted.html')


@skills_app.route("/Contactus")
def sign2():
    return render_template('Contactus.html')


if __name__ == "__main__":
    skills_app.run(debug=True, port=9000)
