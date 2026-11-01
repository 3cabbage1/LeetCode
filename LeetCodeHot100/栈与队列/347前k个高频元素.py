import heapq


# python 小顶堆：
# pri_que=[] #按list初始化
# pri_que[0] #堆头
# heapq.heappush(pri_que,x) # pri_que压入x （若x包含多个元素，如元组[x,y]，先按第一个元素x比，相同再比第二个元素y）
# heapq.heappop(pri_que) # pri_que堆头弹出


# 代码随想录 最优o(nlogk)
# 优先级队列（小顶堆）
# 1. dic存所有元素:频率
# 2. 按频率存入大小k的小顶堆
#    当 堆中元素已>k时pop出堆头
#    （<=>加入一个元素超过k后，将当前最小的一个弹出（可能是这个新数也可能是其他更小的旧数））
# 3. 不断取堆头为前k高频数（原题不要求顺序）
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dic = {}  # {num:频率}
        result = []
        # 1.统计频率
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        # 2. 小顶堆，保证大小为k
        pri_que = []

        for num, freq in dic.items():
            heapq.heappush(pri_que, (freq, num))  # 把元组 (freq, num) 作为一个整体插入堆 pri_que。
            # 堆按 元组比较规则 自动排序：先比第 1 个元素 freq，相等再比第 2 个 num。

            # 加入后size比k大了
            if len(pri_que) > k:
                heapq.heappop(pri_que)  # 弹出当前最小（比里面k个都小）的，保证里面是前k大的

            # 3. 取前k高频
            result.append(heapq.heappop(pri_que)[1])  # 取元组 (freq, num) 里第 2 个 num

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
