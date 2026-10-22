# Definition for singly-linked list.
# 链表题都加虚拟头节点更好做
# 否则需要单独考虑处理head的情况

# 代码随想录版：快慢双指针
# 从fake_head开始，fast走n步就到了第n个节点，
# 所以再f,s一起走到末尾就《=》s到了倒数第n个
# 由于删除要在前一个节点操作指针，即倒数第n+1个
# 因此实际f应先走n+1步再f,s一起走到末尾
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def show(self):
        cur = self
        while cur:
            print(cur.val, end=' ')
            cur = cur.next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 创建一个虚拟节点，并将其下一个指针设置为链表的头部
        dummy_head = ListNode(0, head)

        # 创建两个指针，慢指针和快指针，并将它们初始化为虚拟节点
        slow = fast = dummy_head

        # 快指针比慢指针快 n+1 步
        for i in range(n + 1):
            fast = fast.next

        # 移动两个指针，直到快速指针到达链表的末尾
        while fast:
            slow = slow.next
            fast = fast.next

        # 通过更新第 (n-1) 个节点的 next 指针删除第 n 个节点
        slow.next = slow.next.next

        return dummy_head.next



# # 我的：不好，要一个list来存，空间复杂度O(n)
# class Solution:
#     def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
#         node_list = []
#         fake_head = ListNode()  # 链表题都加虚拟头节点更好做
#         # 否则需要单独考虑处理head的情况
#         fake_head.next = head
#         cur = fake_head
#         while cur:
#             node_list.append(cur)
#             cur = cur.next
#
#         size = len(node_list)
#         index = size - n - 1
#         node_list[index].next = node_list[index + 1].next
#
#         return fake_head.next


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    s.removeNthFromEnd(head, 2).show()
