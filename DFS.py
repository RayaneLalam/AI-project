# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:52:54 2024

@author: rayane
"""
import copy
from collections import deque
from Node import Node


def GraphSearch (Problem, Strategy):
    
    frontier = deque() #Initializing the frontier
    
    
    """
    Before appending the problem state to the frontier, we must convert it to a Node
    using the Node() constructor
    """
    frontier.append(Node(Problem.state))
    
    
    explored = set() #Initializing the explored set
    while frontier :#While the frontier is not empty (there are still nodes that can be expanded)
        if(Strategy == "BFS"):
            node = frontier.popleft() #FIFO
                
        elif Strategy == "DFS":
            node = frontier.pop() # LIFO

        if Problem.is_goal_state(node.state): # Returning the goal
            return node

        explored.add(Node(node.state)) #If the node is not the goal we add it to the explored set

        #If the children are neither in the frontier nor in the explored set, we add them to the explored set
        for child in Problem.expand_node(node, Strategy):
            child_state_tuple = Node(copy.deepcopy(child.state))
                
            if child_state_tuple not in explored and not any(node.state == child.state for node in frontier):
                if Strategy ==  "BFS":
                    frontier.append(child)
                    
                elif Strategy == "DFS":
                    frontier.appendleft(child)

    return None  # failure




        

        
