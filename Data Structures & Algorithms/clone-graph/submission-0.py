"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #clone it first
        #check if theres already a clone of this new node in hashmap
        #if yes == point new node back to first one
        #if no == move on? 
        #recursive one? 

        oldToNew = {} #hashmap

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node] #return new node if it exists. 

            copy = Node(node.val) #clone 
            oldToNew[node] = copy #map old node to copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei)) #return copy we created, and add to neighbours from dfs
            return copy  
        return dfs(node) if node else None

#A more brute force way to think about this problem. This is a good way to think about it before jumping into the solution given by NeetCode.

#1. Use a hashmap to track originals to their clones (same as NC). 
#2. Traverse the original graph, visiting each node once, for each node just clone it's value without the neighbors.
#3. Traverse the original graph again, visiting each node once, for each node find it''s clone and set the original's neighbors clones as the clone's neighbors.
#4. return oldToNew[node]
        
        















        