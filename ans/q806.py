#!/usr/bin/python
# -*- coding:utf8 -*-

class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """

        ws = [widths[ord(a) - 97] for a in S]
        #print ws
        bottle = [0] * len(S)
        full = 0

        for i in ws:
            if bottle[full] + i > 100:
                full = full + 1
                bottle[full] = bottle[full] + i
            else:
                bottle[full] = bottle[full] + i

        return [full+1,bottle[full]]
