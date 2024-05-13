import json
from Land import *
from Country import *


with open('wilaya.json', 'r') as f:
    data = json.load(f)

Lands = {}
index = 1

for country, wilaya in data.items():
    for wilaya, details in wilaya.items():
        Area = details["Area"]
        land = Land(index, index, Area)
        for product, value in details["Products"].items():
            land.set_product_yield(product, value)
        Lands[index] = land
        index += 1 

for land in Lands.values():
    print(land.land_id)
    print(land.product_yields)

InitialState = Country("Algeria", Lands)

selfSufficiency = {
    "Wheat": 10500000,
    "Corn": 9300000,
    "Dates": 600000,
    "Potatoes": 110000000,
    "Tomatoes": 16400000,
    "Green Pepper": 12700000,
    "Aubergines": 126000
  }

goalState = Country("Algeria", {}, selfSufficiency)
