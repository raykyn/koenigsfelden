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

mentions = json.load(open("mentions.json"))

for element in ch["objects"]["municipalities"]["geometries"]:
    name = element["properties"]["name"]
    if name in mentions:
        element["properties"]["mentions"] =  sorted(mentions[name], key=lambda x: x["date"])
    else:
        element["properties"]["mentions"] = []
    
with open("ch_mod_new.json", mode="w") as out:
    json.dump(ch, out)
