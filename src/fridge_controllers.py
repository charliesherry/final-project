from app import app
from flask import request, jsonify, render_template, Flask
from database import db
import requests
from bson.json_util import dumps
from funciones import decode

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/recipes/<ingredient>')
def recipes(ingredient):
    recipes = []
    names = []
    projection = {"title":1,"_id":0}
    hola = db.recipes.find({"ingredients":{"$regex":f"{ingredient}"}},projection)
    for diccionario in hola:
            for key,valor in diccionario.items():
                diccionario[f"{key}"] = decode(diccionario.get(f"{key}"))
            recipes.append(diccionario)
            names.append(valor)
    a = names
    b = f"{ingredient}"

    return render_template("allrecipes.html",variable=[a,b])

@app.route('/prueba2/<recipe>')
def recipesbyingred3(recipe):
    recipes = []
    
    projection = {"title":1,"prep_methods":1,"ingredients":1,"skill_level":1,"serving":1,"chef_name":1,"_id":0,"new_images":1}
    try:
        hola = list(db.recipes.find({"title":f"{recipe}"},projection))
        for diccionario in hola:
            for key,valor in diccionario.items():
                diccionario[f"{key}"] = decode(diccionario.get(f"{key}"))
            recipes.append(diccionario)
        a = recipes[0].get("title")
        b = recipes[0].get("new_images")
        c = recipes[0].get("serving")
        d = recipes[0].get("ingredients")
        e = recipes[0].get("prep_methods")
        f = recipes[0].get("chef_name")
        return render_template("recipes.html",variable = [a,b,c,d,e,f])
    except: raise ValueError("Ingredient not found in db, check your spelling or try another one")

@app.route('/search/level' , methods = ["POST"])
def recipesbydif():
    dif = ["Easy","A challenge", "More effort"]
    recipes1 = []
    names = []
    difficulty = request.form.get("difficulty")
    projection = {"title":1}
    hola = list(db.recipes.find({"skill_level":f" {difficulty} "},projection))
    for diccionario in hola:
            for key,valor in diccionario.items():
                diccionario[f"{key}"] = decode(diccionario.get(f"{key}"))
            recipes1.append(diccionario)
            names.append(valor)
    a = names
    b = f"{difficulty}"
    if difficulty not in dif:
        raise ValueError("Difficulty not found in db. Available difficulties: Easy, More effort, A challenge")
    else: return render_template("allrecipes.html",variable=[a,b])

@app.route('/search', methods = ["POST"])
def recipesbyingreds():
    ingredients = request.form.get("a")
    ingredients = ingredients.split(",")
    recipes = []
    names = []
    projection = {"title":1,"_id":0}
    if len(ingredients) == 2:
        ingredient1 = ingredients[0]
        ingredient2 = ingredients[1]
        try:
            hola = list(db.recipes.find({ "$and": [ {"ingredients":{"$regex":f"{ingredient1}"}},{"ingredients":{"$regex":f"{ingredient2}"}}]},projection))
            for diccionario in hola:
                for key,valor in diccionario.items():
                    diccionario[f"{key}"] = decode(diccionario.get(f"{key}"))
                recipes.append(diccionario)
                names.append(valor)
            a = names
            b = f"{ingredient1},{ingredient2}"
            return render_template("allrecipes.html",variable=[a,b])
        except: raise ValueError("Ingredient not found in db, check your spelling or try another one")
    elif len(ingredients) == 3:
        ingredient1 = ingredients[0]
        ingredient2 = ingredients[1]
        ingredient3 = ingredients[2]
        try:
            hola = list(db.recipes.find({ "$and": [ {"ingredients":{"$regex":f"{ingredient1}"}},{"ingredients":{"$regex":f"{ingredient2}"}},{"ingredients":{"$regex":f"{ingredient3}"}}]},projection))
            for diccionario in hola:
                for key,valor in diccionario.items():
                    diccionario[f"{key}"] = decode(diccionario.get(f"{key}"))
                recipes.append(diccionario)
                names.append(valor)
            a = names
            b = f"{ingredient1},{ingredient2},{ingredient3}"

            return render_template("allrecipes.html",variable=[a,b])
        except: raise ValueError("Ingredient not found in db, check your spelling or try another one")
    elif len(ingredients) == 1:
        ingredient1 = ingredients[0]
        try:
            hola = db.recipes.find({"ingredients":{"$regex":f"{ingredient1}"}},projection)
            for diccionario in hola:
                for key,valor in diccionario.items():
                    diccionario[f"{key}"] = decode(diccionario.get(f"{key}"))
                recipes.append(diccionario)
                names.append(valor)
            a = names
            b = f"{ingredient1}"
            return render_template("allrecipes.html",variable=[a,b])
        except: raise ValueError("Ingredient not found in db, check your spelling or try another one")
