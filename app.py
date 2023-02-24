from flask import Flask, render_template, url_for
import chatgpt_api


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/novel")
def novel():
    return render_template('novel.html')





if __name__ == "__main__":
    app.run(debug=True)