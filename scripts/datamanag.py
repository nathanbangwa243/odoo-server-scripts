#-*- coding: utf-8 -*-

import json

def load_json_data(filename):
    with open(filename, "r") as fp:
        json_data = json.load(fp)
    
    return json_data

def save_json_data(filename, data):
    data_str = json.dumps(data, indent=4)

    with open(filename, "w") as fp:
        fp.write(data_str)
    
def read_data(filename):
    with open(filename, "r") as fp:
        data = fp.read()
    
    return data

def write_data(filename, data):
    with open(filename, "w") as fp:
        fp.write(data)