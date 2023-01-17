# Imports
import json
import os

# Variables
WORK_DIR = os.path.dirname(os.path.realpath(__file__))
raw_path = WORK_DIR + "//..//data//testing//raw"
filename = "//data.json"
filepath = WORK_DIR + "//..//data//testing//harmonized//data.txt"
# Functions

def raw_to_harmonized():
    f = open(raw_path + filename)
    data = json.load(f)
    f.close()
    harmonized = (list(data[0].items()))
    keys = []
    values = []
    for key, value in harmonized:
        keys.append(key)
        values.append(value)
    values = [(tuple(values))]
    print(values)
    return values, keys
    

def to_txt(values, keys, filepath):
    dictionary_h = {}
    for i in range(len(keys)):
        dictionary_h[keys[i]] = values[0][i]
    print(dictionary_h)
    fw = open(filepath, "w")
    fw.write(json.dumps(dictionary_h))
    fw.close()


# Main program
values, keys = raw_to_harmonized()
to_txt(values, keys, filepath)