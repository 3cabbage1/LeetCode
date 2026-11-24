class Solution:
    def __init__(self):
        self.dic = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        self.result = []

    def backtracking(self, digits, letters, cur_index):
        if cur_index == len(digits):
            self.result.append(letters)
            return
        cur = digits[cur_index]
        cur_letters = self.dic[cur]
        for i in cur_letters:
            letters += i
            self.backtracking(digits, letters, cur_index + 1)
            letters = letters[:cur_index]

    def letterCombinations(self, digits: str) -> list[str]:
        self.backtracking(digits, "", 0)
        return self.result


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
