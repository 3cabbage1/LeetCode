# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        result = []
        if not root:
            return result
        queue.append(root)

        while queue:
            # <=>把当前层的节点pop出存进结果list，再添加入下一层节点（即它们的左右孩子）
            size = len(queue)
            for i in range(size):
                cur = queue.pop(0)
                if i == size - 1:
                    result.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    s = Solution()
    print(s.rightSideView(root))
