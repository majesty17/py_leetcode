#!/usr/bin/python
# -*- coding:utf8 -*-

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        length = len(s)
        for i in range(length):
            let_num = ord(s[i]) - 64
            ret=ret+let_num*(26**(length-i-1))

        return ret
