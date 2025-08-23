# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        self.ans = 0
        def diameter(node):
            if node is None:
                return 
            
            left = height(node.left)
            right = height(node.right)
            
            if (left + right) > self.ans:
                self.ans = left + right
            
            diameter(node.left)
            diameter(node.right)



        diameter(root)
        return self.ans