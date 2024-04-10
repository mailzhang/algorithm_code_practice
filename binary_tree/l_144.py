# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def preorder(self, node, preorder_list):
        if not node:
            return
        preorder_list.append(node.val)

        self.preorder(node.left, preorder_list)
        self.preorder(node.right, preorder_list)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        preorder_list = []

        self.preorder(root, preorder_list)

        return preorder_list


if __name__ == '__main__':
    root = TreeNode(1, None,None)
    s = Solution()
    r = s.preorderTraversal(root)
    print(r)