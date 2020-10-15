import pandas as pd
import regex as re
import requests
from bs4 import BeautifulSoup


def decode(lista):
    preps = []
    string = str(lista).replace("\\xa0"," ")
    string1 = string.replace("\u00a0"," ")
    string2 = string1.replace("\\u2028"," ")
    string3 = string2.replace("\"","")
    string4 = string3.replace("\u00e9","e")
    string5 = string4.replace("\u00bd","1/2")
    preps.append(string5)
    return str(preps[0])

def preptime(a):
    """This function obtains the preparation time of each recipe
    Input = URL of the recipe
    Output= Time of preparation, e.g = "10 mins"
    """
    res = requests.get(f'{a}')
    soup = BeautifulSoup(res.text, 'html.parser')
    tag = soup.find_all("time")
    tag = str(tag)
    a  = re.findall(r"\d\d\ \w+",tag)
    try:
        return (a[0])
    except: 
        return "Unknown"

def extractimages(a):
    """This function obtains the main image of each recipe
    Input = URL of the recipe
    Output= Image of the recipe
    """
    resp = requests.get(f"{a}")
    soup = BeautifulSoup(resp.text, 'html.parser')
    tag = soup.find_all("img")[2]
    b = tag["src"]
    return b