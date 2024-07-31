import json
import re

def splitIsotope(isotope):
    parts = re.findall(r"(\d+|[a-zA-Z]+)", isotope)
    return parts

def periodicTable():
    f = open("periodicTable.json")
    return json.load(f)

from reactions_list import reactions 

def loadReactions():
    return reactions