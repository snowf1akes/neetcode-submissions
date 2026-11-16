"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #check for empty node base case
        if not node:
            return None
        oldToNew = {} #hashmap
        queue = deque([node]) #bfs queue seeded with starting node
        oldToNew[node] = Node(node.val) #key value pair, key of original node store clone node

        #pass 1 clone all nodes
       
        #bfs here
        while queue: 
            cur = queue.popleft() #explore next og node
            
            for nei in cur.neighbors: #check for if its been visited already or not
                if nei not in oldToNew: #if not visited
                    oldToNew[nei] = Node(nei.val) #clone new neigbour node
                    queue.append(nei) #add this to queue, todo list to check again later? 
                #skips if its been visited and moves to next node.



        #pass 2 clone all neighbours but its into list
        for old, new in oldToNew.items():
            for nei in old.neighbors:
                new.neighbors.append(oldToNew[nei])

        return oldToNew[node]

