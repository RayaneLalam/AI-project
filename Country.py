from typing import Dict, List
from Land import Land

class Country:
    def __init__(self, name: str, lands: Dict[int, Land], current_production: Dict[str, float] = {
            "Wheat": 0,
            "Corn": 0,
            "Dates": 0,
            "Potatoes": 0,
            "Tomatoes": 0,
            "Green Pepper": 0,
            "Aubergines": 0,
        }):
        self.name = name
        self.lands = {land.land_id: land for land in lands.values()}
        self.current_production = current_production
        # self.current_prices: Dict[str, float] = {
        #     product: float("inf") for product in self.current_production
        # }

    def plant(self, land_id: int, product: str) -> None:
        #if not self.lands[land_id].is_planted:
        self.current_production[product] += self.lands[land_id].get_land_production(product)
            # The price percentage must be calculated in the problem class
            # because self-sufficiency is defined there
            # price_percentage = (
            #     self.lands[land_id].get_land_production(product) * 100
            #     / self.self_sufficiency[product]
            # )
            # self.current_prices[product] *= (1 - price_percentage)


    
    def __ge__(self, other: "Country"):
        for key in self.current_production.keys() :
            if self.current_production[key] < other.current_production[key]:
                return False    
        return True  

    @property
    def empty_lands(self) -> List[Land]:
        return [land for land in self.lands.values() if not land.is_planted]

    def print_production(self) -> None:
        print(self.current_production)


    def __eq__(self, other: "Country"):
        for landId in self.lands.keys():
            if self.lands[landId].PlantedProduct != other.lands[landId].PlantedProduct or self.current_production != other.current_production:
                return False      
        return True
    
    def __hash__(self):
        """
        Define a custom hash function for the Country object.
        This allows Country objects to be used as keys in dictionaries or elements in sets.
        """
        land_hashes = [hash(land) for land in self.lands.values()]
        land_hashes.sort()  # Sort the hashes to ensure consistent ordering
        production_hash = hash(tuple(sorted(self.current_production.items())))
        return hash((tuple(land_hashes), production_hash))

