class Solution:
    def __init__(self):
        self.result=[]

    def backtracking(self, candidates, arr, target,index) -> None:
        if target<0:
            return
        if target==0:
            self.result.append(arr.copy()) # 一定要注意用拷贝！（浅拷贝，因为arr里存的是不可变对象int不是可变对象-引用）
            # 若直接添加arr，是添的引用，后续arr.pop()变了result里的也会变
            return
        for i in range(index,len(candidates)):
            arr.append(candidates[i])
            self.backtracking(candidates,arr,target-candidates[i],i)
            arr.pop()
            if target-candidates[i]<0:
                break


    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        self.backtracking(candidates,[],target,0)
        return self.result


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([8,7,4,3], 11))