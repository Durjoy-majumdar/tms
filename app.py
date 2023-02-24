from flask import *

app=Flask(__name__)

#Rendering a route(Normal Route)
@app.route("/")
def sample():
    return render_template("home.html")

#Rendering/Route -Dynamic Routing
#@app.route("/<name>")
#def sample1(name):
#    return f'Hi {name}'

#template rendering
#@app.route("/template")
#def sample2():
#    return render_template('index.html')

#context to template rendering
#@app.route("/template1/name")
#def sample3(name):
#    return render_template("index2.html", name=name);

if __name__ == '__main__':
    app.run()