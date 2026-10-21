# Definition for singly-linked list.
# 链表题都加虚拟头节点更好做
# 否则需要单独考虑处理head的情况
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
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        node_list = []
        fake_head = ListNode()  # 链表题都加虚拟头节点更好做
        # 否则需要单独考虑处理head的情况
        fake_head.next = head
        cur = fake_head
        while cur:
            node_list.append(cur)
            cur = cur.next

        size = len(node_list)
        index = size - n - 1
        node_list[index].next = node_list[index + 1].next

        return fake_head.next


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    s.removeNthFromEnd(head, 2).show()
