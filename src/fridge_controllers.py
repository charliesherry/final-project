from app import app
from flask import request, jsonify, render_template, Flask
from database import db
import requests
from bson.json_util import dumps
from funciones import decode

@app.route('/')
def hello():
    return render_template('index.html')



#@app.route('/')
#def welcome():
#    return {"message":'Welcome to the Fridge API!'}
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

@app.route('/prueba/<ingredient>')
def recipesbyingred2(ingredient):
    recipes = []
    
    projection = {"title":1,"prep_methods":1,"ingredients":1,"skill_level":1,"serving":1,"chef_name":1,"_id":0,"new_images":1}
    try:
        hola = list(db.recipes.find({"ingredients":{"$regex":f"{ingredient}"}},projection))
        for diccionario in hola:
            for key,valor in diccionario.items():
                diccionario[f"{key}"] = decode(diccionario.get(f"{key}"))
            recipes.append(diccionario)
        a = recipes[0].get("title")
        b = recipes[0].get("new_images")
        c = recipes[0].get("serving")
        d = recipes[0].get("ingredients")
        return render_template("recipes.html",variable = [a,b,c,d])
    except: raise ValueError("Ingredient not found in db, check your spelling or try another one")

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
        return render_template("recipes.html",variable = [a,b,c,d,e])
    except: raise ValueError("Ingredient not found in db, check your spelling or try another one")


@app.route('/search/<ingredient>')
def recipesbyingred(ingredient):
    recipes = []
    projection = {"title":1,"prep_methods":1,"ingredients":1,"skill_level":1,"serving":1,"chef_name":1}
    try:
        for x in db.recipes.find({"ingredients":{"$regex":f"{ingredient}"}},projection):
            recipes.extend([x.get("title"),x.get("serving"),x.get("chef_name"),x.get("skill_level"),
            x.get("prep_methods"),x.get("ingredients")])
        
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

@app.route('/search/<ingredient1>,<ingredient2>,<ingredient3>')
def recipesbyingreds(ingredient1,ingredient2=None,ingredient3=None):
    recipes = []
    projection = {"title":1,"prep_methods":1,"ingredients":1,"skill_level":1,"serving":1,"chef_name":1,"_id":0}
    if ingredient3 == None:
        try:
            hola = list(db.recipes.find({ "$and": [ {"ingredients":{"$regex":f"{ingredient1}"}},{"ingredients":{"$regex":f"{ingredient2}"}}]},projection))
            for diccionario in hola:
                for key,valor in diccionario.items():
                    diccionario[f"{key}"] = decode(diccionario.get(f"{key}"))
                recipes.append(diccionario)
    
            return jsonify(recipes)
        except: raise ValueError("Ingredient not found in db, check your spelling or try another one")
    elif ingredient3 != None:
        try:
            hola = list(db.recipes.find({ "$and": [ {"ingredients":{"$regex":f"{ingredient1}"}},{"ingredients":{"$regex":f"{ingredient2}"}},{"ingredients":{"$regex":f"{ingredient3}"}}]},projection))
            for diccionario in hola:
                for key,valor in diccionario.items():
                    diccionario[f"{key}"] = decode(diccionario.get(f"{key}"))
                recipes.append(diccionario)
    
            return jsonify(recipes)
        except: raise ValueError("Ingredient not found in db, check your spelling or try another one")
        