#!/usr/bin/python
# -*- coding:utf8 -*-

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        str = bin(n).replace("0b", "")

        for i in range(len(str) - 1):
            if str[i] == str[i + 1]:
                return False

        return True
