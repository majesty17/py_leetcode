#!/usr/bin/python
# -*- coding:utf8 -*-

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = []
        for i in A:
            B.append(i[::-1])

        for i in range(len(B)):
            for j in range(len(B[0])):
                B[i][j] = 1 - B[i][j]
        return B
