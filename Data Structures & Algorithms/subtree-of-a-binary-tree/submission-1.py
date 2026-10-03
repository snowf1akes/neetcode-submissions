# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #edge 1: if subroot is null, it will always be subtree of root
        if not subRoot:
            return True

        #edge 2: root is empty, and subroottree isn't emtpy 
        if not root:
            return False

        #call same subtree helper function when both aren't empty 
        if self.sameSubtree(root, subRoot):
            return True 

        #not same tree, but not empty 
        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))

    def sameSubtree(self, root, subRoot):

        #both null
        if not root and not subRoot:
            return True
        #both null + same vals
        if root and subRoot and root.val == subRoot.val:
            return (self.sameSubtree(root.left, subRoot.left) and 
            self.sameSubtree(root.right, subRoot.right)) 
        #1 empty, 1 non empty
        return False
        