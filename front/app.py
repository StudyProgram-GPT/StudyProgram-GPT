from flask import Flask, render_template, request, jsonify
import requests


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit_code", methods=["POST"])
def submit_code():
    code = request.form["code"]
    url = "http://localhost:8080//content"  # ここにバックエンドのURLを入れてください
    response = requests.post(url, data={"code": code})
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(debug=True)
    print("hello")
