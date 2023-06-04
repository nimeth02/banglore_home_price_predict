import json
import pickle

import numpy as np

_locations=['hoo']
data_columns=None
model=None

def get_estimated_price(location,sqft,bhk,bath):
    global data_columns
    global _locations
    global model
    with open("./artifects/columns.json", "r") as f:
        data_columns = json.load(f)['data_columns']
        _locations = data_columns[3:]
    with open("./artifects/banglore_model.pickle", "rb") as f:
        model = pickle.load(f)
    print("loading saved artifacts... done")
    try:
        loc_index=data_columns.index(location.lower())
    except:
        loc_index=-1
    x=np.zeros(len(data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index >= 0:
        x[loc_index]=1
    return round(model.predict([x])[0],2)


def get_location_names():
    global _locations

    with open("./artifects/columns.json", "r") as f:
        data_columns = json.load(f)['data_columns']
        _locations = data_columns[3:]
        return _locations

def load_saved_artifects():
    print('loading artifects ... start')
    global data_columns
    global _locations
    global model
    with open("./artifects/columns.json","r") as f:
        data_columns=json.load(f)['data_columns']
        _locations=data_columns[3:]
    with open ("./artifects/banglore_home_prices_model.pickle","rb") as f:
        model=pickle.load(f)
    print("loading saved artifacts... done")

if __name__ == "__main__":
    load_saved_artifects()
    print(get_location_names())
    print(get_estimated_price('Kalhalli',1000,2,2))
