# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if s is None:
            return 0
        elif self.isSametree(s,t):
            return 1
        else:
            return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        
    def isSametree(self, s, t):
        if s is None or t is None:
            return s is None and t is None
        if (s.val == t.val):
            return self.isSametree(s.left, t.left) and self.isSametree(s.right,t.right)
