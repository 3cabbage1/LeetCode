class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        暴力解法
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    if nums[i] + nums[j] == target:
                        return [i, j]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
