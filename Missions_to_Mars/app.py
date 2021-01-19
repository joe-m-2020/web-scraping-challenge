# Import Flask
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
# create app
app=Flask(__name__)

# PyMongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_to_mars")

# route
@app.route("/")
def home():

    mars_info = mongo.db.collection.find_one()

    return render_template("index.html", mars=mars_info)

@app.route("/scrape")
def scrape():

    # run scrape function
    mars_data = scrape_mars.scrape_data()

    #update mongo db using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back home
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)