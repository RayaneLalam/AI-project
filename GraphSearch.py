# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:41:22 2024

@author: rayane
"""

import heapq  # Priority Queue
from Node import Node
from collections import deque
import random




def GraphSearch(Problem, Strategy, MaxDepth=float('inf'), MaxCost=float('inf')):
    
    frontier = Frontier(Strategy, Problem)

    nonExpanded = [] #The nodes that went over the MaxCost or MaxDepth
    explored = set() #Initializing the explored set
    
    while not frontier.isEmpty() :#While the frontier is not empty (there are still nodes that can be expanded)
    
        node = frontier.pop()
                                    
        if node.depth > MaxDepth: #Specific to Iterative deepening
            return None, len(explored) + 1
        
        if node.estimatedCost + node.cost > MaxCost: #Specific to Iterative Deepening A* / Best First
            heapq.heappush(nonExpanded, node)
            
        else:       
            if Problem.is_goal_state(node.state): # Returning the goal
                return node, len(explored) + 1
            
            if Strategy != "StochasticHillClimbing" and Strategy != "SteepestAscent": #Because local search does not care about the explored nodes
                explored.add(Node(node.state)) #If the node is not the goal we add it to the explored set
            
            for child in Problem.expand_node(node, Strategy):                    
                if child not in explored and not any(node.state == child.state for node in frontier.frontier):  
                    
                    if Strategy == "StochasticHillClimbing":
                        if child < node: #Only better successors
                            frontier.push(child)
                    else:             
                        frontier.push(child)
                                  
    print("Solution not found")
    if nonExpanded: #If nonExpanded is not empty (specific to depth limited)
        firstRefusedNode = heapq.heappop(nonExpanded) # this is the node with the minimum value that went over the threshhold
        return firstRefusedNode.cost + firstRefusedNode.estimatedCost, len(explored) #We return the cost of this node
    return node, len(explored)  # failure


"""Uninformed search"""


# BFS
def BreadthFirstSearch(Problem):
    return GraphSearch(Problem, "BFS")


# UCS
def UniformCostSearch(Problem):
    return GraphSearch(Problem, "UCS")


# DFS
def DepthFirstSearch(Problem):
    return GraphSearch(Problem, "DFS")


# Depth Limited
def DepthLimitedSearch(Problem, MaxDepth):
    return GraphSearch(Problem, "DFS", MaxDepth, float("inf"))


# Iterative Deepening
def IterativeDeepeningSearch(Problem, MaxDepth):
    Solution = None
    i = 0
    TotalNumberOfNodes = 0
    while Solution == None and i <= MaxDepth:
        Solution, NumberOfNodes = DepthLimitedSearch(Problem, i)
        i += 1
        TotalNumberOfNodes += NumberOfNodes
    return Solution, TotalNumberOfNodes


"""Informed search"""

# Greedy Best First Search
def GreedyBestFirstSearch(Problem):
    return GraphSearch(Problem, "Greedy")


# A*
def A_star(Problem):
    return GraphSearch(Problem, "A_star")


# Cost Limited A* is like Depth Limited Search with a MaxCost
# For each Node we must have f = g + h <= MaxCost
def CostLimitedAstar(Problem, CostLimit):
    return GraphSearch(Problem, "CostLimited", float("inf"), CostLimit)


# Iterative Deepening Cost Limited A*
def IterativeDeepeningAstar(Problem, CostLimit):
    Solution = None
    i = 0
    TotalNumberOfNodes = 0
    while i <= CostLimit:
        Solution, NumberOfNodes = CostLimitedAstar(Problem, i)
        TotalNumberOfNodes += NumberOfNodes
        if isinstance(Solution, Node):
            return Solution, TotalNumberOfNodes
        elif Solution != None:
            i = Solution
    return None


def CostLimitedBestFirst(Problem, CostLimit):
    return GraphSearch(Problem, "CostLimitedBestFirst", float("inf"), CostLimit)


# Iterative Deepening Cost Limited A*
def IterativeDeepeningBestFirst(Problem, CostLimit):
    Solution = None
    i = 0
    TotalNumberOfNodes = 0
    while i <= CostLimit:
        Solution, NumberOfNodes = CostLimitedBestFirst(Problem, i)
        TotalNumberOfNodes += NumberOfNodes
        if isinstance(Solution, Node):
            return Solution, TotalNumberOfNodes
        elif Solution != None:
            i = Solution
    return None


def StochasticHillClimbing(Problem):
    return GraphSearch(Problem, "StochasticHillClimbing")


def SteepestAscent(Problem):
    return GraphSearch(Problem, "SteepestAscent")


class Frontier:
    # frontier.push(Node(Problem.state, None, None, 0, Problem.heuristic(Node(Problem.state))))

    def __init__(self, Strategy, Problem):
        self.Strategy = Strategy
        if (
            Strategy == "DFS"
            or Strategy == "BFS"
            or Strategy == "CostLimited"
            or Strategy == "CostLimitedBestFirst"
        ):
            self.frontier = deque()  # Initializing the LIFO frontier

        elif (
            Strategy == "Greedy"
            or Strategy == "A_star"
            or Strategy == "UCS"
            or Strategy == "StochasticHillClimbing"
            or Strategy == "SteepestAscent"
        ):
            self.frontier = []  # Initializing the frontier as a priority queue

        # Pushing the initial State with the right estimated cost
        if Strategy == "DFS" or Strategy == "BFS":
            self.frontier.append(Node(Problem.state))

        elif Strategy == "UCS":
            heapq.heappush(self.frontier, Node(Problem.state))

        elif (
            Strategy == "Greedy"
            or Strategy == "A_star"
            or Strategy == "StochasticHillClimbing"
            or Strategy == "SteepestAscent"
        ):
            heapq.heappush(
                self.frontier,
                Node(
                    Problem.state, None, None, 0, Problem.heuristic(Node(Problem.state))
                ),
            )  # Pushes and keeps the list sorted

        elif Strategy == "CostLimited" or Strategy == "CostLimitedBestFirst":
            self.frontier.appendleft(
                Node(
                    Problem.state, None, None, 0, Problem.heuristic(Node(Problem.state))
                )
            )

    def push(self, node):
        if self.Strategy == "BFS" or self.Strategy == "StochasticHillClimbing":
            self.frontier.append(node)

        elif (
            self.Strategy == "DFS"
            or self.Strategy == "CostLimited"
            or self.Strategy == "CostLimitedBestFirst"
        ):
            self.frontier.appendleft(node)

        elif (
            self.Strategy == "Greedy"
            or self.Strategy == "A_star"
            or self.Strategy == "UCS"
        ):
            heapq.heappush(self.frontier, node)  # Pushes and keeps the list sorted

        # elif self.Strategy == "SteepestAscent":
        #     if

    def pop(self):
        if self.Strategy == "BFS":
            node = self.frontier.popleft()  # FIFO

        elif (
            self.Strategy == "Greedy"
            or self.Strategy == "A_star"
            or self.Strategy == "UCS"
        ):
            node = heapq.heappop(self.frontier)

        elif (
            self.Strategy == "DFS"
            or self.Strategy == "CostLimited"
            or self.Strategy == "CostLimitedBestFirst"
            or self.Strategy == "SteepestAscent"
        ):
            node = self.frontier.pop()

        elif self.Strategy == "StochasticHillClimbing":
            node = random.choice(self.frontier)
            self.frontier = []

        return node

    def makeEmpty(self):
        self.frontier = []

    def isEmpty(self):
        return not self.frontier