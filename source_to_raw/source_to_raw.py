# imports
import pandas as pd
import requests
import os

# variables
WORK_DIR = os.path.dirname(os.path.realpath(__file__))
raw_path = WORK_DIR + "//..//data//testing//raw"
filename = "//data.json"
url_1 = "https://swapi.dev/api/people/1/"
keys = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url']
pd.set_option('display.max_rows', None)

# functions
def source_to_raw(url, filename):
    r = requests.get(url)
    print(r.raise_for_status())
    json = r.json()
    print(json)
    df = pd.json_normalize(json)
    df.to_json(raw_path + filename, orient='records')
    
    



# main_program
source_to_raw(url_1, filename)