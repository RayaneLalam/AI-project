from typing import Dict, List
from Wilaya import Wilaya
from Land import Land

class Country:

    def __init__(self, name: str, wilayas: Dict[int, Wilaya], current_production: Dict[str, float] = {
            "Wheat": 0,
            "Corn": 0,
            "Dates": 0,
            "Potatoes": 0,
            "Tomatoes": 0,
            "Green Pepper": 0,
            "Aubergines": 0,
        }):
        self.name = name
        self.wilayas = {wilaya.Id: wilaya for wilaya in wilayas.values()}
        self.current_production = current_production
        # self.current_prices: Dict[str, float] = {
        #     product: float("inf") for product in self.current_production
        # }

    def plant(self, wilayaId: int, product: str) -> None:
        if len(self.wilayas[wilayaId].empty_lands) > 0:
            self.current_production[product] += self.wilayas[wilayaId].plant(product)
            # The price percentage must be calculated in the problem class
            # because self-sufficiency is defined there
            # price_percentage = (
            #     self.lands[land_id].get_land_production(product) * 100
            #     / self.self_sufficiency[product]
            # )
            # self.current_prices[product] *= (1 - price_percentage)


    def nonfullWilaya(self):
        for wilaya in self.wilayas.values():
            if len(wilaya.empty_lands) > 0:
                return wilaya.Id


    def __ge__(self, other: "Country"):
        for key in self.current_production.keys() :
            if self.current_production[key] < other.current_production[key]:
                return False    
        return True  

    @property
    def empty_lands(self, wilayaId) -> List[Land]:
        return self.wilayas[wilayaId].empty_lands()

    def print_production(self) -> None:
        print(self.current_production)
        for key in self.wilayas.keys():
            for plantedLand in self.wilayas[key].planted_lands:
                print("Wilaya", key, "Planted with product", plantedLand.PlantedProduct, "at land", plantedLand.land_id)



    def __eq__(self, other: "Country"):
        for wilayaId in self.wilayas.keys():
            if not self.wilayas[wilayaId] == other.wilayas[wilayaId] or self.current_production != other.current_production:
                return False      
        return True
    
    def __hash__(self):
        return hash((self.name, frozenset(self.wilayas.keys()), frozenset(self.current_production.items())))

