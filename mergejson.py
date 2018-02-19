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

with open("placenames.tsv") as placenames:
    reader = csv.reader(placenames, delimiter="\t")
    for row in reader:
        if row[3] not in ["???", "DE"]:
            c[row[3]] += int(row[1])
        
#~ print(ch["objects"]["municipalities"]["geometries"][0]["properties"]["name"])

for element in ch["objects"]["municipalities"]["geometries"]:
    name = element["properties"]["name"]
    
    if name in c:
        element["properties"]["occ"] = c[name]
    else:
        element["properties"]["occ"] = 0
        
with open("ch_mod.json", mode="w") as out:
    json.dump(ch, out)
