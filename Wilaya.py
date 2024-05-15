from typing import Dict, List
from Land import Land

class Wilaya:

    PRODUCTS = ["Wheat", "Corn", "Dates", "Potatoes", "Tomatoes", "Green Pepper", "Aubergines"]


    def __init__(self, wilayaId, Area, numberOfLands):
        self.Id = wilayaId
        lands: Dict[int, Land] = {}
        #self.lands = {land.land_id: land for land in lands.values()}
        self.Area = Area
        self.numberOfLands = numberOfLands
        self.product_yields = {}
        for i in range(numberOfLands):
            landId = wilayaId * 100 + i
            lands[landId] = Land(self.Id, landId, self.Area / self.numberOfLands)
        self.lands = lands
        



    @property
    def available_products(self):
        """Return a list of available products."""
        return self.product_yields.copy()
    

    def set_product_yield(self, product: str, yield_per_hectare: float):
        """Set the yield per hectare for a given product."""
        if product not in self.PRODUCTS:
            raise ValueError(f"Invalid product: {product}")
        if yield_per_hectare != 0:
            self.product_yields[product] = yield_per_hectare
            for land in self.lands.values():
                land.set_product_yield(product, yield_per_hectare)




    @property
    def empty_lands(self) -> List[Land]:
        return [land for land in self.lands.values() if not land.is_planted]
    
    @property
    def planted_lands(self) -> List[Land]:
        return [land for land in self.lands.values() if land.is_planted]
    
    def plant(self, product: str):
        if len(self.empty_lands) > 0:
            return self.empty_lands[0].get_land_production(product)

    def __eq__(self, other: "Wilaya"):
        return self.Id == other.Id and set(self.lands.values()) == set(other.lands.values()) 
    
    def __ne__(self, other: "Wilaya"):
        return not self == other
    
    def __hash__(self):
        return hash((self.Id, frozenset(self.lands.values()), self.Area))