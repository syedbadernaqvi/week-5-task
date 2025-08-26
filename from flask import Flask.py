from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return "Hello Home Page"

@app.route("/about")
def about():
    return "Hello About Page"

if _name_ == "_main_":
    app.run(debug=True)