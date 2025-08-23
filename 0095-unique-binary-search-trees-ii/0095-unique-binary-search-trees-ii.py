# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def bst(start, end):
            if start > end:
                return [None]
            
            trees = []
            for root_val in range(start, end+1):
                left_tree = bst(start, root_val - 1)
                right_tree = bst(root_val + 1, end)

                for l in left_tree:
                    for r in right_tree:
                        root = TreeNode(root_val)
                        root.left = l
                        root.right = r
                        trees.append(root)
            return trees
        return bst(1, n)