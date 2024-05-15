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
Wilayas : dict[int, Wilaya] = {}
index = 1


for country, wilaya in data.items():

    for wilaya, details in wilaya.items():
        newWilaya = Wilaya(index, details["Area"], details["NumberLands"])
        
        for product, value in details["Products"].items():
            if value != 0:
                newWilaya.set_product_yield(product, value)
        Wilayas[index] = newWilaya
        index += 1



"""for w in Wilayas.values():
    for land in w.lands.values():
        print(land.product_yields)
        break"""

InitialState = Country("Algeria", Wilayas)

selfSufficiency = {
    "Wheat": 10500,
    "Corn": 9300,
    "Dates": 60,
    "Potatoes": 1100,
    "Tomatoes": 1640,
    "Green Pepper": 1270,
    "Aubergines": 1260
  }

goalState = Country("Algeria", Wilayas, selfSufficiency)




problem = AgricultureProblem(InitialState, goalState)


SolveProblem(problem)



