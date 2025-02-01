"""
    144. 二叉树的前序遍历
    给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
    示例 1：
            输入：root = [1,null,2,3]
            输出：[1,2,3]
    示例 2：
            输入：root = [1,2,3,4,5,null,8,null,null,6,7,9]
            输出：[1,2,4,5,6,7,3,8,9]
    示例 3：
            输入：root = []
            输出：[]
    示例 4：
            输入：root = [1]
            输出：[1]
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.preorder(root, res)
        return res

    def preorder(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)
