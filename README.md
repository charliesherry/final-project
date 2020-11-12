# What's in your fridge? (Ironhack's Final Project)
![image](https://blog.gunassociation.org/wp-content/uploads/2013/04/fridge-bg.jpg)

## Introduction:
The idea of this project is to create an API that gives us recipes given some search querys, like ingredients or difficulties.

## Work done:
- First, the recipes data set was extracted and cleaned in Jupyter notebook.
- Then, the clean data was uploaded to MongoDB for further uses.
- The API was created and personalized with HTML in order to make it functional.
- (TDB) Deployed on Heroku for public use

## How to use it (locally):
- Execute src/server.py in order to initialize the server
- Open your browser on localhost:5000
- Search for recipes with ingredients (3 max) or difficulty (Easy, Medium and Hard)
- A list of recipes will apear, click the link on any of these and you will be redirected to a full description of this recipe

## Material Used:
- Python
- Flask
- Beautifoul Soup
- Requests
- MongoDB
- Heroku
- HTML and CSS

### Documentation:
- https://www.kaggle.com/venkataganesh/recipes-clean-dataset
- https://flask.palletsprojects.com/en/1.1.x/
- https://es.python-requests.org/es/latest/user/quickstart.html
