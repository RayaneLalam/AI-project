from Wilaya import Wilaya
from Land import Land

firstLand = Land(1, 101, 10)
firstLand.PlantedProduct = "Wheat"

secondLand = Land(1, 102, 10)
secondLand.PlantedProduct = "Corn"

dict1 = {
    101: firstLand,
    102: secondLand
}

wilaya1 = Wilaya(2, dict1, 20)


third = Land(1, 101, 10)
third.PlantedProduct = "Corn"

fourth = Land(1, 102, 10)
fourth.PlantedProduct = "Wheat"

dict2 = {
    101: third,
    102: fourth
}

wilaya2 = Wilaya(1, dict2, 20)





