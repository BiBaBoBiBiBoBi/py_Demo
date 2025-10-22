import math
from typing import List, Optional
from collections import deque
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        result = list()

        while q:
            size = len(q)
            sub_queue = list()
            while size > 0:
                tree_node = q.popleft()
                sub_queue.append(tree_node.val)

                left_node = tree_node.left
                right_node = tree_node.right
                if left_node:
                    q.append(left_node)
                if right_node:
                    q.append(right_node)
                size -= 1
            result.append(sub_queue)
        print(f"{result}")
        return result

    # 给你一棵二叉树的根节点 root ，请你判断这棵树是否是一棵 完全二叉树 。
    # 在一棵 完全二叉树 中，除了最后一层外，所有层都被完全填满，并且最后一层中的所有节点都尽可能靠左。
    # 最后一层（第 h 层）中可以包含 1 到 2h 个节点。
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root])
        has_null = False

        while q:
            node = q.popleft()
            if node is None:
                has_null = True
                continue
            if has_null:
                return False
            q.append(node.left)
            q.append(node.right)

        return True

    def traversal_preorder(self,curr: Optional[TreeNode],res:List[int]):
        if not curr:
            return
        res.append(curr.val)
        self.traversal_preorder(curr.left,res)
        self.traversal_preorder(curr.right,res)

    def traversal_postorder(self,curr: Optional[TreeNode],res:List[int]):
        if not curr:
            return
        self.traversal_postorder(curr.left,res)
        self.traversal_postorder(curr.right,res)
        res.append(curr.val)

    #给你二叉树的根节点 root ，返回它节点值的 前序 遍历
    # 前序， 中左右
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        self.traversal_preorder(root,res)
        return res

    # 后序：左右中
    # 前中后 ， 就是指当前节点的遍历顺序 ，即： 中左右，左中右，左右中
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traversal_postorder(root, res)
        return res

if __name__ == '__main__':
    lst = [1, None, 2, 3, None]
    print(f"{lst.index(None)}")
