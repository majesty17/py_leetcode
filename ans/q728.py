#!/usr/bin/python
# -*- coding:utf8 -*-


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ret = []
        for i in range(left, right + 1):
            if (self.isit(i)):
                ret.append(i)

        return ret

    def isit(self, num):

        for i in str(num):
            if i=="0":
                return False
            if num%(int(i))!=0:
                return False
        return True