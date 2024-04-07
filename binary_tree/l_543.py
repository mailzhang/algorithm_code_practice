# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    length = 0

    def deep_tree(self, node):
        if not node:
            return 0
        left = self.deep_tree(node.left)
        right = self.deep_tree(node.right)
        max_deep = max(left, right) + 1
        if self.length < left + right:
            self.length = left + right

        return max_deep

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.deep_tree(root)
        return self.length
