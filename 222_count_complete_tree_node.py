# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        #made use of property of complete tree
        if not root:
            return 0
        
        left_h = self.depth(root.left)
        right_h = self.depth(root.right)
        
        if left_h == right_h:
            return (1<<left_h) + self.countNodes(root.right)
        else:
            return (1<<right_h) + self.countNodes(root.left)
        
        
    def depth(self, node):
        if not node: return 0
        return 1 + self.depth(node.left)