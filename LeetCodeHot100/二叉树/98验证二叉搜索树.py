# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 代码随想录：二叉搜索树《=》中序遍历序列升序
class Solution:

    # 力扣最好写实例属性，怀疑力扣多个测试案例都是在一个文件里一起运行验证的
    # 因为写在外面是类属性，而可变的类属性会被多个实例共享，可能留下残余
    # 比如：
    # a = Solution()
    # b = Solution()
    # a.mid.append(0)
    # print(b.mid)  # [0]，b 看到了 a 留下的内容
    # 两个对象共享的可变类属性可能残余
    # （类属性若是直接使用了=赋值才会创建一个新的同名实例属性覆盖，
    # 这里是可变对象，直接使用的append更改，所以不会被覆盖）
    def __init__(self):
        self.mid = []

    def midOrder(self, root: TreeNode):
        if not root:
            return None
        self.midOrder(root.left)
        self.mid.append(root.val)
        self.midOrder(root.right)

    def isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        self.midOrder(root)
        for i in range(1, len(self.mid)):
            if self.mid[i] <= self.mid[i - 1]:
                return False
        return True


# 我的：时间复杂度太高了，不推荐
# class Solution:
#     def findMin(self,root,min_val):
#         if not root:
#             return min_val
#         if root.val<min_val:
#             min_val=root.val
#         min_val=self.findMin(root.left,min_val)
#         min_val=min(min_val,self.findMin(root.right,min_val))
#         return min_val
#
#     def findMax(self,root,max_val):
#         if not root:
#             return max_val
#         if root.val>max_val:
#             max_val=root.val
#         max_val=self.findMax(root.left,max_val)
#         max_val=max(max_val,self.findMax(root.right,max_val))
#         return max_val
#     def isValidBST(self, root: TreeNode | None) -> bool:
#         # 边界条件
#         if not root:
#             return True
#
#         # 当前节点判断：能否保证 左子树最大值<root<右子树最小值
#         if root.left and root.val<=self.findMax(root.left,root.left.val):
#             return False
#         if root.right and root.val>=self.findMin(root.right,root.right.val):
#             return False
#
#         return self.isValidBST(root.left) and self.isValidBST(root.right) # 还要保证左右子树都是二叉搜索树


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    print(s.isValidBST(root))
