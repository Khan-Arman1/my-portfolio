from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # return "<h1>Hello World!</h1>"
    return render_template("index.htm")

@app.route('/contact')
def contact():
    return render_template("contact.htm")

# @app.route('/bot')
# def bot():
#     return "Bot Page"

if __name__ == "__main__":
    app.run(debug=True, port=8004)