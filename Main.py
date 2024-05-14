from GraphSearch import *
from Node import *
from Problem import *
import json
from Land import *
from Country import *

def SolveProblem(Problem: AgricultureProblem):
    Reverseresult = None
    result = [] #Stores the path to the goal in reverse order (From the goal to the root)
    
    listOfStrategies = ["BFS", "DFS", "UCS", "Depth Limited Search", "Iterative Deepening Search",
                        "A*", "Greedy Best First Search", "Cost Limited Depth First Search",
                        "Iterative Deepening A*", "Cost Limited Best First", "Iterative Deepening Best First",
                        "Stochastic Hill Climbing"
                        ]
    for i in range(len(listOfStrategies)):
        print(i + 1, listOfStrategies[i])
        
    Strategy = input("\nChoose your Strategy: ")
    
    if Strategy == "1":
        Reverseresult, NumberOfNodes = BreadthFirstSearch(Problem)#Goal state
    elif Strategy == "2":
        Reverseresult, NumberOfNodes = DepthFirstSearch(Problem)#Goal state
    elif Strategy == "3":
        Reverseresult, NumberOfNodes = UniformCostSearch(Problem)#Goal state
    elif Strategy == "4":
        DepthLimit = int(input("Enter your depth limit: "))
        Reverseresult, NumberOfNodes = DepthLimitedSearch(Problem, DepthLimit)#Goal state
    elif Strategy == "5":
        DepthLimit = int(input("Enter your depth limit: "))
        Reverseresult, NumberOfNodes = IterativeDeepeningSearch(Problem, DepthLimit)#Goal state
    elif Strategy == "6":
        Reverseresult, NumberOfNodes = A_star(Problem)#Goal state
    elif Strategy == "7":
        Reverseresult, NumberOfNodes = GreedyBestFirstSearch(Problem)#Goal state
    elif Strategy == "8":
        CostLimit = int(input("Enter your cost limit: "))
        Reverseresult, NumberOfNodes = CostLimitedAstar(Problem, CostLimit)#Goal state
    elif Strategy == "9":
        CostLimit = int(input("Enter your cost limit: "))
        Reverseresult, NumberOfNodes = IterativeDeepeningAstar(Problem, CostLimit)#Goal state
    elif Strategy == "10":
        CostLimit = int(input("Enter your cost limit: "))
        Reverseresult, NumberOfNodes = CostLimitedBestFirst(Problem, CostLimit)#Goal state
    elif Strategy == "11":
        CostLimit = int(input("Enter your cost limit: "))
        Reverseresult, NumberOfNodes = IterativeDeepeningBestFirst(Problem, CostLimit)#Goal state
    elif Strategy == "12":
        Reverseresult, NumberOfNodes = StochasticHillClimbing(Problem)#Goal state

    print("\n")

    #We retrieve the path to the goal by starting from the goal
    #And climbing the tree (since every node has access to its parent)
    if isinstance(Reverseresult, Country):
        Reverseresult.print_production()
    else:
        print(Reverseresult)
                    
    print("Number of visited Nodes: ", NumberOfNodes)






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



"""for land in Lands.values():
    print(land.land_id)
    print(land.product_yields)"""

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

goalState = Country("Algeria", Lands, selfSufficiency)

"""newstate = copy.deepcopy(goalState)
for product, value in newstate.current_production.items():
    newstate.current_production[product] += 100000000000000


goalState.print_production()
newstate.print_production()"""

#InitialState.plant(1, "Wheat")
"""newstate = copy.deepcopy(InitialState)
print(newstate.lands[1].isPlanted)"""


problem = AgricultureProblem(InitialState, goalState)


SolveProblem(problem)

#problem.expand_node(Node(InitialState), "DFS")


