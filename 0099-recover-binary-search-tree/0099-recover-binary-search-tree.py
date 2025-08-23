# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        
        result = list()
        def inorder(node):
            if node is not None:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)
        inorder(root)
        swap_a, swap_b = None, None
        for j in range(len(result)-1,0,-1):
            for i in range(j):
                if result[i] > result[j]:
                    swap_a, swap_b = result[i], result[j]
                    break
            if swap_a is not None: break
            
        def traverse(node):
            if node is not None:
                traverse(node.left)
                if node.val == swap_a:
                    node.val = swap_b
                elif node.val == swap_b:
                    node.val = swap_a
                traverse(node.right)
        
        traverse(root)