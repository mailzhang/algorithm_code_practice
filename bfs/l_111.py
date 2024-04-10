# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
import collections


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue_ = collections.deque()
        queue_.append(root)
        row_ = 1
        while queue_:
            r_len = len(queue_)
            for i in range(r_len):
                item = queue_.popleft()
                if item.right is None and item.left is None:
                    return row_
                if item.right:
                    queue_.append(item.right)
                if item.left:
                    queue_.append(item.left)
            row_ += 1
        return row_
