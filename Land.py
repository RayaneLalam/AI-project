class Land:
    """Represents a land area (wilaya) in Algeria."""

    PRODUCTS = ["Wheat", "Corn", "Dates", "Potatoes", "Tomatoes", "Green Pepper", "Aubergines"]

    def __init__(self, wilaya_id: int, land_id: int, area: float, state = False):
        self.wilaya_id = wilaya_id
        self.land_id = land_id
        self.area = area
        self.isPlanted = False
        self.PlantedProduct = None
        self.product_yields = {}

    @property
    def available_products(self):
        """Return a list of available products."""
        return self.product_yields.copy()

    def set_product_yield(self, product: str, yield_per_hectare: float):
        """Set the yield per hectare for a given product."""
        if product not in self.PRODUCTS:
            raise ValueError(f"Invalid product: {product}")
        self.product_yields[product] = yield_per_hectare

    def get_land_production(self, product: str) -> float:
        """Get the total production of a given product on the land."""
        if product not in self.product_yields:
            raise ValueError(f"Yield not set for product: {product}")
        self.isPlanted = True
        self.PlantedProduct = product
        yield_per_hectare = self.product_yields[product]
        return self.area * yield_per_hectare

    @property
    def is_planted(self):
        """Check if any product is planted on the land."""
        return self.isPlanted