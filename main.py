from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    with open("count.txt") as f:
        count = int(f.read())        
    return render_template("index.html", count=count)

@app.post("/add")
def add():
    with open("count.txt") as f:
        count = int(f.read())

    with open("count.txt", "w") as f:
        f.write(str(count + 1))
    return "Done"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="6979")