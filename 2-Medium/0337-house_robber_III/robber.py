# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode | None) -> int:
        
        # Returns a list/tuple: [money_if_robbed, money_if_skipped]
        def dfs(node: TreeNode | None) -> list[int]:
            if not node:
                return [0, 0]
            
            # Post-order traversal: Solve left and right subtrees first
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Choice 1: Rob this node. 
            # Must skip the immediate left and right children.
            rob_this = node.val + left[1] + right[1]
            
            # Choice 2: Skip this node.
            # We can choose the max available from each child independently.
            skip_this = max(left) + max(right)
            
            return [rob_this, skip_this]
            
        return max(dfs(root))