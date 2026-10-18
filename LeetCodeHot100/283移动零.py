class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast,slow = 0,0
        while fast < len(nums):
            if nums[fast] == 0:
                fast+=1
            else:
                nums[slow]=nums[fast]
                slow+=1
                fast+=1
        while slow < len(nums):
            nums[slow] = 0
            slow+=1
        print(nums)

if __name__ == '__main__':
    s = Solution()
    s.moveZeroes([0,1,0,3,12])