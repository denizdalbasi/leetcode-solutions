class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode | None) -> int:
        
        def dfs(node: TreeNode | None) -> list[int]:
            if not node:
                return [0, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            rob_this = node.val + left[1] + right[1]
            
            skip_this = max(left) + max(right)
            
            return [rob_this, skip_this]
            
        return max(dfs(root))