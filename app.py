import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Cookbook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/cookbook')
def cookbook():
    return render_template("cookbook.html", recipes=mongo.db.recipes.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
                           categories=mongo.db.categories.find())

@app.route('/metrics')
def metrics():
    return render_template('metrics.html',
                           categories=mongo.db.metrics.find())




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
