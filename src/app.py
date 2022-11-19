from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
  return render_template("index.html")

@app.route("/trabalhos")
def trabalhos():
  return render_template("trabalhos.html")

@app.route("/familia")
def familia():
  return render_template("familia.html")

if __name__ == "__main__":
  app.run(debug = True)
