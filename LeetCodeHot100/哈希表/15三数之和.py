# 代码随想录 双指针，一个当 cur，另外两个双指针 left、right分成从头和尾向中间逼近
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 代码随想录 双指针
        nums=sorted(nums)
        result=[]
        for i in range(len(nums)-2):
            # print(f"nums[i]={nums[i]}")
            left, right = i+1, len(nums) - 1
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                # 前面已经用过相同的cur了，跳过
                continue
            while left<right:
                if nums[i]+nums[left]+nums[right]<0:
                    # left 和当前最大的right加都小了，left++
                    left+=1
                elif nums[i]+nums[left]+nums[right]>0:
                    right-=1
                else:
                    if left>i+1 and left<right and right<len(nums)-1:
                        if nums[left]==nums[left-1] and nums[right]==nums[right+1]:
                            # 针对 0, 0,0,...,0,0 或 -1, -1,-1,...,1,1型
                            right -= 1
                            left += 1
                            continue
                    result.append([nums[i],nums[left],nums[right]])
                    right -= 1
                    left += 1

        return result







    # 时间复杂度太高了，重复放入再去重带来的开销多
    # 因此，最好在放入前就判断不要重复
    # def threeSum(self, nums: list[int]) -> list[list[int]]:
    #     dic={} #{当前值:index}
    #     result=[]
    #     for i in range(len(nums)-2):
    #         target = 0-nums[i]
    #         for j in range(i+1,len(nums)):
    #             if target-nums[j] in dic :
    #                 result.append(tuple(sorted([nums[i],nums[j],target-nums[j]])))
    #                 dic[nums[j]]=j
    #             elif target-nums[j] not in dic:
    #                 dic[nums[j]] = j
    #         dic={}
    #     result=set(result)
    #     result=list(result)
    #     return result
if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([0,0,0,0,0,0,0,0]))