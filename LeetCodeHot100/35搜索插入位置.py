class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """左闭右闭[left,right]"""
        left = 0
        right = len(nums) - 1

        return self.search(nums, target, left, right)

    def search(self, nums: list[int], target: int, left: int, right: int) -> int:

        if target < nums[left]:
            return left
        elif target > nums[right]:
            return right + 1
        cur = (left + right) // 2

        if target == nums[cur]:
            return cur
        elif target > nums[cur]:
            return self.search(nums, target, cur + 1, right)
        else:
            return self.search(nums, target, left, cur - 1)


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 5, 6]
    target = 3
    print(s.searchInsert(nums, target))
