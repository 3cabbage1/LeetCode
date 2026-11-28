class Solution:
    def __init__(self):
        self.result = []
        self.arr = []

    def isValid(self, str):
        for i in range(len(str)):
            if str[i] != str[len(str) - i - 1]:
                return False
        return True

    # 根据代码随想录的顺一下逻辑：
    # aab：按切割位置1,2,3：a|ab、aa|b、aab|
    # 再切子串
    def backtracking(self, s):
        if not s:
            self.result.append(self.arr.copy())
            return
        for i in range(1, len(s) + 1):
            if self.isValid(s[:i]):
                self.arr.append(s[:i])
                self.backtracking(s[i:])
                self.arr.pop()

    def partition(self, s: str) -> list[list[str]]:
        self.backtracking(s)
        return self.result


if __name__ == '__main__':
    s = Solution()
    print(s.partition('cdd'))

    # 1.0:逻辑有点乱
    # def backtracking(self,s,index):
    #     if len(s)>1:
    #         if self.isValid(s):
    #             self.arr.append(s)
    #             self.result.append(self.arr.copy())
    #             self.arr.pop()
    #
    #     if index==len(s):
    #         self.arr.append(s)
    #         self.result.append(self.arr.copy())
    #         self.arr.pop()
    #         return
    #     for i in range(index,len(s)):
    #         if self.isValid(s[:i]):
    #             self.arr.append(s[:i])
    #             self.backtracking(s[i:],1)
    #             self.arr.pop()
    #
    #
    # def partition(self, s: str) -> list[list[str]]:
    #     self.backtracking(s,1)
    #     return self.result
