# 左括号直接入栈
# 右括号能与栈顶匹配则栈顶pop；否则非法 False

class Solution:
    def isValid(self, s: str) -> bool:
        signs = {'(': 0, ')': 1, '{': 2, '}': 3, '[': 4, ']': 5}
        stack = []
        # python 栈用list实现(先入后出FILO)
        # not stack :栈非空
        # stack[-1] :栈非空前提下取栈顶
        # stack.append(1) :push
        # stack.pop() :pop
        for char in s:
            if not stack:
                if signs[char] % 2 == 0:
                    stack.append(char)
                else:
                    return False
            else:
                if signs[char] % 2 == 0:
                    stack.append(char)
                else:
                    if signs[stack[-1]] // 2 == signs[char] // 2:  # python整除是//   而/默认算成浮点数
                        stack.pop()
                    else:
                        return False
        return True if not stack else False


if __name__ == '__main__':
    s = Solution()
    print(s.isValid('()[]{}'))
