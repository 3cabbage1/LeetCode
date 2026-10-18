# 本题相当于普通二分查找只是在找到mid==target后的情况下新增了一个找是否左右还有边界的问题
# 对于找不到的情况其实还是和之前一样的
#
# O(logn) 二分查找的思想，每次只取一半区间继续进行查找
# 所以找到mid==target后再做两次二分查找，再左右半区间分别查找是否还有左右target边界
# O(logn)+O(logn)==O(logn)
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        """左闭右闭[left,right]"""
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                def search_left(left1: int, right1: int) -> int:
                    l_r = mid  # 嵌套函数内可读前面的外部变量，但不能直接赋值（赋值操作默认创建新的局部变量，除非先声明nonlocal）
                    while left1 <= right1:
                        mid1 = (left1 + right1) // 2
                        if nums[mid1] < target:
                            left1 = mid1 + 1
                        elif nums[mid1] > target:
                            right1 = mid1 - 1
                        else:
                            right1 = mid1 - 1
                            l_r = mid1  # 等于时更新

                    return l_r

                def search_right(left2: int, right2: int) -> int:
                    r_r = mid
                    while left2 <= right2:
                        mid2 = (left2 + right2) // 2
                        if nums[mid2] < target:
                            left2 = mid2 + 1
                        elif nums[mid2] > target:
                            right2 = mid2 - 1
                        else:
                            left2 = mid2 + 1
                            r_r = mid2  # 等于时更新

                    return r_r

                return [search_left(left, mid - 1), search_right(mid + 1, right)]

        return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 11))

# <=>线性探索，最坏情况相当于遍历查找而非二分查找一半一半区间的查找，退化为O(n),需要优化为O(logn)
# class Solution:
#     def searchRange(self, nums: list[int], target: int) -> list[int]:
#         """左闭右闭[left,right]"""
#         left, right = 0, len(nums) - 1
#
#         while left <= right:
#             cur = (left + right) // 2
#             if target > nums[cur]:
#                 left = cur + 1
#             elif target < nums[cur]:
#                 right = cur - 1
#             else:
#                 if nums[left]==target and nums[right]==target:
#                     return [left, right]
#                 if nums[left] != target:
#                     left += 1 # <=>线性探索，最坏情况相当于遍历查找，退化为O(n)
#                 if nums[right] != target:
#                     right -= 1 # <=>线性探索，最坏情况相当于遍历查找，退化为O(n)
#
#         return [-1, -1]
# ### 所以需要改进为 O(logn)
