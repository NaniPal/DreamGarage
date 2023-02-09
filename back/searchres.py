from flask import Flask, render_template, request
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
#connection mongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["garage"]
collection = db["main"]

@app.route("/", methods=["GET", "POST"])
@app.route("/search")
def search():
   if request.method == "POST":
        table_name = request.form.get("table_name")

        # Execute the query
        results = collection.find({})

        # Render the results in an HTML template
        return render_template("results.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)