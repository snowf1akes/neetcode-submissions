# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.prev = float('-inf')
    
        def inorder(node):
            if not node:
                return True
            
            if not inorder(node.left): #validate left tree fully
                return False
            
            #visit + check new node has to be larger than previous otherwise not bst
            if node.val <= self.prev:
                return False

            self.prev = node.val
            return inorder(node.right)
        return inorder(root)
    
    
