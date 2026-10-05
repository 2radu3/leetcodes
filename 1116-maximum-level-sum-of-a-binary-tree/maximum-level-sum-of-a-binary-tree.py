# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        maxval = 0
        q = collections.deque([root])
        res = []
        i = 0
        level = 1
        maxval, maxlevel = None, None

        while q:
            total = 0
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                total += node.val #for -> each node on the level gets added to total
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)

            if maxval == None:
                    maxval = total
                    maxlevel = level

            if total > maxval:
                    maxval = total
                    maxlevel = level

            level += 1
        
        return maxlevel

           
                
        