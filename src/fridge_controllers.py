from app import app
from flask import request, jsonify
from database import db
import requests
from bson.json_util import dumps

@app.route('/')
def welcome():
    return {"message":'Welcome to the Fridge API!'}

@app.route('/search/<ingredient>')
def recipesbyingred(ingredient):
    collection = db.recipes 
    projection = {"title":1,"prep_methods":1}
    #recipes=db.recipes.find({"ingredients":{"$regex":f"{ingredient}"}})
    for x in db.recipes.find({"ingredients":{"$regex":f"{ingredient}"}},projection):
        title = x.get("title")
        prep = x.get("prep_methods")
        ingred = x.get("ingredients")

        result = {
            "title" : title,
            "preparation" : prep,
            "ingredients":ingred
        }
    try:
        return dumps(result)
    except: raise ValueError("Ingredient not found in db, check your spelling or try another one")

@app.route('/search/level/<difficulty>')
def recipesbydif(difficulty):
    collection = db.recipes 
    projection = {"title":1,"prep_methods":1}
    #recipes=db.recipes.find({"ingredients":{"$regex":f"{ingredient}"}})
    for x in db.recipes.find({"skill_level":f" {difficulty} "},projection):
        title = x.get("title")
        prep = x.get("prep_methods")
        ingred = x.get("ingredients")

        result = {
            "title" : title,
            "preparation" : prep,
            "ingredients":ingred
        }
    try:
        return jsonify(result)
    except: raise ValueError("Difficulty not found in db. Available difficulties: Easy, More effort, A challenge")
