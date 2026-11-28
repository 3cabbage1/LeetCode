class Solution:
    def __init__(self):
        self.dic = {}
        self.result = [[]]
        self.arr = []

    def backtracking(self, nums, index):
        if index >= len(nums):
            return
        for i in range(index, len(nums)):
            self.arr.append(nums[i])
            self.result.append(self.arr.copy())
            self.backtracking(nums, i + 1)
            self.arr.pop()

    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.backtracking(nums, 0)
        return self.result


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([]))
