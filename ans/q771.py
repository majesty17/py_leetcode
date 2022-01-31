#!/usr/bin/python
# -*- coding:utf8 -*-


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        sum=0
        for i in J:
            sum=sum+S.count(i)
        return sum