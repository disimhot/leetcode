# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        return depth_search(root, 1)

def depth_search(node, depth):
    if node.left is None and node.right is None:
        return depth

    if node.left is None:
        return depth_search(node.right, depth + 1)

    if node.right is None:
        return depth_search(node.left, depth + 1)

    return  max(depth_search(node.left, depth + 1), depth_search(node.right, depth + 1))
