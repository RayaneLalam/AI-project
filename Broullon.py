import json
from Land import *

with open('wilaya.json', 'r') as f:
    data = json.load(f)

Lands = {}
index = 1


for country, wilaya in data.items():

    for wilaya, details in wilaya.items():
        index_land = 100 * index
        Area = details["Area"] / details["NumberLands"]
        for i in range(details["NumberLands"]):
            land = Land(index, index_land, Area)
            for product, value in details["Products"].items():
                land.set_product_yield(product, value)
            Lands[index_land] = land
            index_land += 1
        index += 1

for land in Lands.values():
    print(land.land_id)
