#!/usr/bin/python
# -*- coding:utf8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        root = TreeNode(t1.val + t2.val)
        self.doMerge(root, t1, t2)
        return root

    def doMerge(self, root, t1, t2):
        if t1 == None and t2 == None:
            root = None
            return

        if t1 == None:
            root.left = t2.left
            root.right = t2.right
            return

        if t2 == None:
            root.left = t1.left
            root.right = t1.right
            return

        root.left = TreeNode(t1.left.val + t2.left.val)

        self.doMerge(root.left, t1.left, t2.left)
        root.right = TreeNode(t1.right.val + t2.right.val)
        self.doMerge(root.right, t1.right, t2.right)
