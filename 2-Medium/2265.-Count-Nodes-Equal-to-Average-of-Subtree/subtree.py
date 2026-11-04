# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        _, _, matching_nodes = self.dfs(root)
        return matching_nodes

    def dfs(self, node: TreeNode) -> tuple[int, int, int]:
        if not node:
            return (0, 0, 0)  

        left_sum, left_count, left_matches = self.dfs(node.left)
        right_sum, right_count, right_matches = self.dfs(node.right)

        subtree_sum = left_sum + right_sum + node.val
        subtree_count = left_count + right_count + 1

        is_match = 1 if (subtree_sum // subtree_count == node.val) else 0
        total_matches = left_matches + right_matches + is_match

        return (subtree_sum, subtree_count, total_matches)