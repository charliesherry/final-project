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
    recipes = []
    projection = {"title":1,"prep_methods":1,"ingredients":1,"skill_level":1,"serving":1}
    for x in db.recipes.find({"ingredients":{"$regex":f"{ingredient}"}},projection):
        recipes.append(x.get("title"))
        recipes.append(x.get("serving"))
        recipes.append(x.get("skill_level"))
        recipes.append(x.get("prep_methods"))
        recipes.append(x.get("ingredients"))
        
    try:
        return jsonify(recipes)
    except: raise ValueError("Ingredient not found in db, check your spelling or try another one")

@app.route('/search/level/<difficulty>')
def recipesbydif(difficulty):
    dif = ["Easy","A challenge", "More effort"]
    recipes1 = []
    projection = {"title":1,"prep_methods":1,"ingredients":1}
    for x in db.recipes.find({"skill_level":f" {difficulty} "},projection):
        recipes1.append(x.get("title"))
        recipes1.append(x.get("prep_methods"))
        recipes1.append(x.get("ingredients"))
    if difficulty not in dif:
        raise ValueError("Difficulty not found in db. Available difficulties: Easy, More effort, A challenge")
    else: return jsonify(recipes1)
