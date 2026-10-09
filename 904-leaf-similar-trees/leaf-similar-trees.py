# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def DFS(root: TreeNode, leaves: list[int]):
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root.val)
                return
            DFS(root.left, leaves)
            DFS(root.right, leaves)
        res1: list[int] = []
        res2: list[int] = []

        DFS(root1, res1)
        DFS(root2, res2)
        return res1 == res2
        