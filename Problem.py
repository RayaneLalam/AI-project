from __future__ import annotations
from typing import List
import copy
from Node import Node
from Country import Country
from collections import deque
import time



class AgricultureProblem:



    def __init__(self, initial_state: Country, goal_state: Country):
        self.state = initial_state
        self.goal_state = goal_state
        self.numberOfChildren = 0


    def is_goal_state(self, goal_test: Country) -> bool:
        """
        Check if the given state (goal_test) meets or exceeds the goal state.
        """
        return goal_test >= self.goal_state
    
    def printNod(self, node: Node):
        state : Country = node.state
        state.print_production()

    def expand_node(self, node: Node, Strategy) -> List[Node]:
        """
        Expand the given node by generating all possible child nodes.
        """
        ProductSufficiency : bool = False #Becomes true when a ccertain product reaches self sufficiency in UCS
        state: Country = node.state
        child_nodes = []
        """node.state.print_production()
        print("\n\n")
        print("Parent node: ")
        node.state.print_production()
        print("Children nodes: ")"""
        wilayaId = state.nonfullWilaya()
        OverPlantedProduct : list = []
        for product in state.wilayas[wilayaId].available_products:
            next_state = copy.deepcopy(state)
            if self.goal_state.current_production[product] - next_state.current_production[product] <= 0:                    
                OverPlantedProduct.append(product)
            next_state.plant(state.wilayas[wilayaId].Id, product)
            if product not in OverPlantedProduct:
                if self.goal_state.current_production[product] - next_state.current_production[product] <= 0:
                    childPathCost = 0
                else:
                    childPathCost = node.cost + (self.goal_state.current_production[product] - next_state.current_production[product]) / self.goal_state.current_production[product]
            else:
                childPathCost = float('inf')

            #next_state.print_production()
            self.numberOfChildren += 1
            if Strategy == "BFS":
                child_nodes.append(Node(next_state, parent=node))
            elif Strategy == "DFS":
                child_nodes.insert(0, Node(next_state, parent=node))
            elif Strategy == "UCS":
                #print(childPathCost)
                child_nodes.append(Node(next_state, node, None, childPathCost, 0))
    

        """print(self.numberOfChildren)
        print("\n\n")
        time.sleep(0.5)"""
        return child_nodes


        
    
    def pathCost(self, node):
        """
        Returns goal_test.production - node.production
        """
        pass



        