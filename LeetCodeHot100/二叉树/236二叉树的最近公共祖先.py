# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归，后序遍历，左右中

class Solution:
    def __init__(self):
        self.ancestor = None

    def solute(self, root, p, q):
        if not root:
            return 0
        count = 0
        # 左
        count_left = self.solute(root.left, p, q)
        if count_left == 2: # 左子树里已找齐，直接返回
            return 2
        # 右
        count_right = self.solute(root.right, p, q)
        if count_right == 2: # 右子树里已找齐，直接返回
            return 2
        # root
        if root.val == p.val or root.val == q.val:
            count += 1
        count += count_left + count_right
        if count == 2: # root 为最近祖先
            self.ancestor = root
        return count

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.solute(root, p, q)
        return self.ancestor


if __name__ == '__main__':
    s = Solution()
