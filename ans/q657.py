#!/usr/bin/python
# -*- coding:utf8 -*-

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        u = moves.count("U")
        d = moves.count("D")
        r = moves.count("R")
        l = moves.count("L")
        if (u == d) and (r == l):
            return True
        return False
