# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        cur = head
        new_node = ListNode()
        while cur:
            if cur == head:
                new_node.val = cur.val
                new_node.next = None
            else:
                tem_node = ListNode(cur.val, new_node)
                new_node = tem_node
            cur = cur.next
        return new_node


if __name__ == '__main__':
    s = Solution()
    node3 = ListNode(3, None)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    print(s.reverseList(node1).val)
