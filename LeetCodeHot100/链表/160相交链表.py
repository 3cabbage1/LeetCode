# Definition for singly-linked list.
# 快慢双指针，基于19删除链表的倒数第N个节点拓展
# 《=》n是短的那个链表长度，找长的那个链表的倒数第n个，
# 然后再和短的个headB开始比较走
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def show(self):
        cur = self
        while cur:
            print(cur.val, end=' ')
            cur = cur.next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        fastA, slowA = headA, headA
        fastB, slowB = headB, headB
        isOneEnd = False  # 一个链表已到最后一个结点
        result = None
        while fastA.next or fastB.next:
            if not fastA.next and not isOneEnd:
                # 若A更短，为统一A都为长的一个，交换
                # tem_fastA = fastA
                # tem_slowA = slowA
                # fastA = fastB
                # slowA=slowB
                # fastB =tem_fastA
                # slowB=tem_slowA
                fastA, fastB = fastB, fastA  # python 交换可简写
                slowA, slowB = slowB, slowA
            fastA = fastA.next
            if not isOneEnd:
                if not fastB.next:  # B 到最后一个
                    isOneEnd = True
                else:
                    fastB = fastB.next
            if isOneEnd:
                slowA = slowA.next
        while slowA and slowB:
            if slowA == slowB and not result:
                result = slowA
            elif slowB != slowA:
                result = None
            slowA = slowA.next
            slowB = slowB.next
        return result
