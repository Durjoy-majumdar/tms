from flask import *

app=Flask(__name__)

#Rendering a route(Normal Route)
@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/home")
def sample():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("/login.html")

@app.route("/register")
def register():
    return render_template("/register.html")

@app.route("/aboutus")
def aboutus():
    return render_template("/aboutus.html")

if __name__ == '__main__':
    app.run()