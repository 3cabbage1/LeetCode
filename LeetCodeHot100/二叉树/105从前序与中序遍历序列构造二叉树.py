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
            size=len(queue)

            for i in range(size):
                cur = queue.pop(0)
                print(cur.val,end=" ")
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            print()


# 前序第一个定中间节点作分割点
# 将中序分割为左右子区间
# 根据中序分割的左右子区间的长度再分前序的左右子区间
# 递归

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        # 均左闭右闭
        in_left = []  # inorder中的左子区间
        in_right = []  # inorder中的右子区间
        pre_left = []
        pre_right = []
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                in_left = inorder[:i]
                in_right = inorder[i + 1:]
                pre_left = preorder[1:i + 1]
                pre_right = preorder[i + 1:]
        root.left =self.buildTree(pre_left, in_left)
        root.right =self.buildTree(pre_right, in_right)
        return root

if __name__ == '__main__':
    s = Solution()
    s.buildTree([1,2], [2,1]).show()