from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/start")
def start():
    return "<p>Start Watch</p>"

@app.route("/stop")
def stop():
    return "<p>Stop Watch</p>"

@app.route("/reset")
def reset():
    return "<p>Reset Watch</p>"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)