# 用一个哈希表存遍历过的值和对应index，供后面的查前面有没有刚好是我差的值target-nums[i]
class Solution:
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     """
    #     暴力解法
    #     """
    #     for i in range(len(nums)):
    #         for j in range(len(nums)):
    #             if j != i:
    #                 if nums[i] + nums[j] == target:
    #                     return [i, j]
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """哈希表解法"""
        dic = {}  # {值:index}
        result = []
        for i in range(len(nums)):
            find = target - nums[i]  # 差的值
            if find in dic:
                result.append(dic[find])
                result.append(i)
                return result
            else:
                dic[nums[i]] = i
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
