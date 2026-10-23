# fast走2步，slow走1步《=》fast相对于slow速度为1
# 所以有环则一定会相遇，且是在环内相遇
# 按head、环起点、f和s相遇点 划分，根据2倍关系
# (!!!注意，这里有坑，为保证满足两倍关系，一定要在fast_count%2==0时才判断两者是否相遇，否则不一定满足2倍关系)
# (或者用slow = slow.next
#       fast = fast.next.next
# 的形式)
# 可证 x=(n-2n'-1)(y+z)+z
# 即 index1 从 head 出发走 x 到环起点 《=》index2从 相遇点 出发走(n-2n'-1)圈后再走z步
# 就会和 index1 在环起点相遇


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def detectCycle(self, head: ListNode) ->ListNode:
        fast,slow = head,head
        fast_count=0
        encounter=None # fast and slow 的相遇点
        while fast:
            fast = fast.next
            fast_count+=1
            if fast_count%2==0:
                slow = slow.next
                ### !!!
                if fast==slow and fast: # 为保证f走的是s的两倍关系，一定要在fast_count%2==0时判断两者是否相遇
                    # (或者在最开始用 slow = slow.next
                    #              fast = fast.next.next
                    # 的形式)
                    encounter=fast
                    break

        if not encounter:
            return None
        else:
            index1=head
            index2=encounter
            while index1!=index2:
                index1=index1.next
                index2=index2.next
            return index1


if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    tem=ListNode(4)
    tem.next = head.next
    head.next.next.next = tem

    print(Solution().detectCycle(head).val)