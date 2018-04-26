#! /usr/bin/python3

from collections import Counter
import csv
import json

# load the json as a dict
# count the appearance of every commune
# find the corresponding nodes in the json, add the value, else add 0
# dump a new json with what we need

c = Counter()

ch = json.load(open("ch.json"))

mentions = json.load(open("mentions_2.json"))

for element in ch["objects"]["municipalities"]["geometries"]:
    name = element["properties"]["name"]
    if name in mentions:
        element["properties"]["mentions"] =  sorted(mentions[name], key=lambda x: x["date"])
    else:
        element["properties"]["mentions"] = []
        
# TODO: make a separate ch_mod file in which all the non Swiss Cities
de_cities = {
    "Waldshut" : [957, 114],
    "Säckingen" : [870, 145],
    "Dogern" : [945, 118],
    "Wien" : [1500, 250],
    "Beuggen" : [829, 136],
    "Bergheim (Haut-Rhin)" : [650, 100],
    "Stunzingen": [953, 110],
    "Konstanz" : [1248, 84],
    "Eberfingen" : [1020, 66],
    "Küssaberg" : [980, 116]
    }
    
de_json = []
    
for n, (key, item) in enumerate(de_cities.items()):
    de_json.append({"id":n, "name":key, "mentions":sorted(mentions[key], key=lambda x: x["date"]), "coords":item})
    
    
with open("ch_mod_new.json", mode="w") as out:
    json.dump(ch, out)
    
with open("de_places.json", mode="w") as out:
    json.dump(de_json, out)

