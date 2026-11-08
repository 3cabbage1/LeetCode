# 我这里是用None隔开每一层
# 可看代码随想录用每层的size来做
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#         queue = collections.deque([root])
#         result = []
#         while queue:
#             level = []
#             for _ in range(len(queue)):
#                 cur = queue.popleft()
#                 level.append(cur.val)
#                 if cur.left:
#                     queue.append(cur.left)
#                 if cur.right:
#                     queue.append(cur.right)
#             result.append(level)
#         return result


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        queue = []
        result = []
        tem_r = []
        if not root:
            return result
        queue.append(root)
        queue.append(None)
        while queue:
            cur = queue[0]
            if not cur:
                result.append(tem_r)
                tem_r = []
                queue.pop(0)
                if queue:
                    queue.append(None)
                continue

            tem_r.append(cur.val)
            queue.pop(0)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return result


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(s.levelOrder(root))
