# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False

        all_sum = []

        def sum(node, val):
            if node.left is None and node.right is None:
                val += node.val
                all_sum.append(val)
                return

            val += node.val

            if node.left is not None:
                sum(node.left, val)
            if node.right is not None:
                sum(node.right, val)

        sum(root, 0)
        print(all_sum)
        return targetSum in all_sum

