#!/usr/bin/python
# -*- coding:utf8 -*-

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        ret = []
        for i in range(numRows):

            row = []
            for j in range(i+1):
                row.append(self.c(i,j))

            ret.append(row)

        return ret
    def c(self,n,m):
        import math
        f=math.factorial(n)
        s=math.factorial(m)
        t=math.factorial(n-m)
        return f/(s*t)
