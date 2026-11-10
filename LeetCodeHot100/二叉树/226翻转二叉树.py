# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def show(self):
        queue=[]
        queue.append(self)
        while queue:
            size = len(queue)
            for i in range(size):
                cur=queue.pop(0)
                print(cur.val,end=' ')
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            print()


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # tem_left=root.left
        # root.left = self.invertTree(root.right)
        # root.right = self.invertTree(tem_left)
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(4)
    t.left = TreeNode(2)
    t.right = TreeNode(7)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    t.right.left = TreeNode(6)
    t.right.right = TreeNode(9)
    # t.show()
    Solution().invertTree(t).show()