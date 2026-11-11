# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 代码随想录：递归，比较根节点下左右节点内外侧是否相同
class Solution:
    def compare(self, left, right):
        if not left and not right:
            return True
        elif left and right:
            if left.val != right.val:
                return False
            else:
                return self.compare(left.left, right.right) and self.compare(left.right, right.left)
        else:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.compare(root.left, root.right)


# # 我的：带当层None的层序，每层比较是否对称
# 能过，就是遍历细节要慢慢处理
# class Solution:
#     def isSymmetric(self, root: TreeNode | None) -> bool:
#         queue = []
#         result = []
#         if root == None:
#             return True
#         queue.append(root)
#         while queue:
#             size = len(queue)
#             tem_q = []
#             isAllNone = True
#             for i in range(size):
#                 cur = queue.pop(0)
#                 tem_q.append(cur)
#                 if cur:
#                     queue.append(cur.left)
#                     queue.append(cur.right)
#                     isAllNone = False
#             if not isAllNone:
#                 result.append(tem_q)
#             else:
#                 break
#
#         for i in range(len(result)):
#             if i == 0:
#                 continue
#             for j in range(len(result[i]) // 2):
#                 if result[i][j] and result[i][len(result[i]) - j - 1]:
#                     if result[i][j].val != result[i][len(result[i]) - j - 1].val:
#                         return False
#                 elif not result[i][j] and not result[i][len(result[i]) - j - 1]:
#                     continue
#                 else:
#                     return False
#         return True


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    root.left.right.left = TreeNode(5)
    root.left.right.right = TreeNode(6)
    root.right.left.left = TreeNode(6)
    root.right.left.right = TreeNode(5)
    #
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(2)
    # root.left.left = TreeNode(3)
    # root.right.right = TreeNode(3)
    # root.left.left.left = TreeNode(4)
    # root.right.right.right = TreeNode(4)
    print(Solution().isSymmetric(root))
