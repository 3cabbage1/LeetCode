# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        # 虚拟头节点，加上更统一，否则需要单独特殊处理节点为head的情况
        fake_head = ListNode()
        fake_head.next = head
        cur = fake_head
        if not cur.next or not cur.next.next: # python '非' 是 not
            return cur.next
        cur_next = cur.next
        cur_next_next = cur.next.next
        cur_next_next_next = cur.next.next.next
        while cur_next and cur_next_next:
            cur.next=cur_next_next
            cur_next_next.next =cur_next
            cur_next.next=cur_next_next_next

            cur = cur.next.next
            if not cur.next or not cur.next.next:
                break
            cur_next = cur.next
            cur_next_next = cur.next.next
            cur_next_next_next = cur.next.next.next
        return fake_head.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    s = Solution()
    print(s.swapPairs(head).val)
