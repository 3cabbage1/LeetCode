# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# # 代码随想录：
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#
#         def dfs(node):
#             if node is None:
#                 return
#
#             dfs(node.left)
#             res.append(node.val)
#             dfs(node.right)
#
#         dfs(root)
#         return res

# 我的
class Solution:
    def inorder(self, root, l):
        if not root:
            return None
        self.inorder(root.left, l)
        l.append(root.val)
        self.inorder(root.right, l)

    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        self.inorder(root, result)
        return result
