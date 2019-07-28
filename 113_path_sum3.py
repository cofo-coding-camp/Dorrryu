# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        self.res = []
        self.dfs(root, [], sum)
        return self.res
        
    def dfs(self, node, path, sum):
        #if not node.left and not node.right and node.val == sum:
        #    self.res.append(path+[node.val])
        if node.left:
            self.dfs(node.left, path+[node.val], sum-node.val)
        if node.right:
            self.dfs(node.right, path+[node.val], sum-node.val)
        if not node.left and not node.right and node.val == sum:
            self.res.append(path+[node.val])