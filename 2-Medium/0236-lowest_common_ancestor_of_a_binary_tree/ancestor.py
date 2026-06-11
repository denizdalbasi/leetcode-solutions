# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base Case: if we hit a null node or find one of our targets
        if not root or root == p or root == q:
            return root
            
        # Recurse on the left and right subtrees
        left_result = self.lowestCommonAncestor(root.left, p, q)
        right_result = self.lowestCommonAncestor(root.right, p, q)
        
        # If both subtrees returned a valid node, the current root is the LCA
        if left_result and right_result:
            return root
            
        # Otherwise, return whichever side found a target node (or None if both are None)
        return left_result if left_result else right_result