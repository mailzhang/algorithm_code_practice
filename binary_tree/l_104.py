# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    deep = 0
    max_deep = 0

    def f_tree(self, node):
        if node is None:
            return
        self.deep += 1
        if node.left is None and node.right is None:
            if self.deep > self.max_deep:
                self.max_deep = self.deep
        self.f_tree(node.left)
        self.f_tree(node.right)

        self.deep -= 1

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.f_tree(root)
        return self.max_deep
