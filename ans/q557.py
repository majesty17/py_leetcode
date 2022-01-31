#!/usr/bin/python
# -*- coding:utf8 -*-

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = []
        ws = s.split(" ")
        for i in ws:
            ret.append(i[::-1])
        return " ".join(ret)
