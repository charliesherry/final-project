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