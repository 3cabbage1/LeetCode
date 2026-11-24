# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 我的，有点像二分，找中间的做当前root，然后递归不断分左右子树
class Solution:
    def solute(self, nums, left, right):
        # 左闭右闭
        if left > right:
            return None
        cur_index = (left + right) // 2
        root = TreeNode(nums[cur_index])
        root.left = self.solute(nums, left, cur_index - 1)
        root.right = self.solute(nums, cur_index + 1, right)
        return root

    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        return self.solute(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
