# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0;
        else:
            return 1 + self.goodNodesHelper(root.left, root.val) +  self.goodNodesHelper(root.right, root.val)

    def goodNodesHelper(self, n: TreeNode, maxVal: int) -> int:
        if n is None:
            return 0;
        if n.val >= maxVal:
            return 1 + self.goodNodesHelper(n.left, n.val) + self.goodNodesHelper(n.right, n.val)
        else:
            return self.goodNodesHelper(n.left, maxVal) + self.goodNodesHelper(n.right, maxVal)

        