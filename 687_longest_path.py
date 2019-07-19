# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.len = 0
        self.dfs(root)
        return self.len

    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        left_path = right_path = 0

        if node.left and node.val == node.left.val:
            left_path = left + 1
        if node.right and node.val == node.right.val:
            right_path = right + 1
        self.len = max(self.len, left_path+right_path)
        return max(left_path, right_path)
