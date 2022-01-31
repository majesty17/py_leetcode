#!/usr/bin/python
# -*- coding:utf8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        h1 = l1
        h2 = l2
        a = []
        while True:
            if (h1 is None) and (h2 is None):
                break;
            sum = 0
            if h1 != None:
                sum += h1.val
                h1 = h1.next
            if h2 != None:
                sum += h2.val
                h2 = h2.next
            a.append(sum)

        for i in range(len(a) - 1):
            if a[i] >= 10:
                a[i] = a[i] - 10
                a[i + 1] = a[i + 1] + 1

        if a[-1] >= 10:
            a[-1] = a[-1] - 10
            a.append(1)

        root = ListNode(a[0])
        pt = root

        for i in a[1:]:
            pt.next = ListNode(i)
            pt = pt.next
            pt.next=None

        return root
