from __future__ import annotations
from typing import List
import copy
from Node import Node
from Country import Country
import time

class AgricultureProblem:
    def __init__(self, initial_state: Country, goal_state: Country):
        self.state = initial_state
        self.goal_state = goal_state

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
        state: Country = node.state
        child_nodes: List[Node] = []
        node.state.print_production()
        for land in state.empty_lands:
            for product in land.available_products:
                next_state = copy.deepcopy(state)
                next_state.plant(land.land_id, product)
                next_state.print_production()
                child_nodes.append(Node(next_state, parent=node))
        print(len(child_nodes))
        print("\n\n")
        time.sleep(30)
        return child_nodes
    
    def pathCost(self, node):
        """
        Returns goal_test.production - node.production
        """
        pass



        