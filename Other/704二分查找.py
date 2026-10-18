class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return self.search2(nums, target, 0, len(nums) - 1)

    def search2(self, nums: list[int], target: int, left: int, right: int) -> int:
        """双闭，[left,right]"""
        if left > right:
            return -1
        cur = int((right + left) / 2)
        if nums[cur] == target:
            return cur
        if target > nums[cur]:
            return self.search2(nums, target, cur + 1, right)
        else:
            return self.search2(nums, target, left, cur - 1)


if __name__ == "__main__":
    s = Solution()
    # s.search([-1, 0, 3, 5, 9, 12], 9)
    print(s.search([-1, 0, 3, 5, 9, 12], 2))
