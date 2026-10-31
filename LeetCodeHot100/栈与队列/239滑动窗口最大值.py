import collections


# 暴力：O(n*k)
# 代码随想录 单调队列：O(n)
# 维持的单队：以当前滑动窗口内最大值开始，单减的数字队列
class MonotonicQueue:
    """自定义单调队列维护"""

    def __init__(self):
        self.queue = collections.deque()

    def front(self):
        return self.queue[0]

    def tail(self):
        return self.queue[-1]

    def push(self, num):
        if not self.queue or num < self.tail():
            self.queue.append(num)
        else:
            while self.queue and num > self.tail():  # 把前面<它的值都pop后再push，保证单↓
                self.queue.pop()
            self.queue.append(num)

    def pop(self, num):
        # 因为维持的单调队列（相对顺序不变，只是选择能组成单减的元素入队），
        # 所以队头永远在前面（即队头下标<其他单队里的元素的下标）
        # （即维持的单队：以当前滑动窗口内最大值开始，单减的数字队列）
        """只在队头（max）出队时更新queue"""
        if self.queue and num == self.front():  # 当前队列非空才能取队头
            self.queue.popleft()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mq = MonotonicQueue()
        result = []
        for i in range(k):
            mq.push(nums[i])
        result.append(mq.front())
        for i in range(1, len(nums) - k + 1):
            mq.pop(nums[i - 1])
            mq.push(nums[i + k - 1])
            result.append(mq.front())
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
