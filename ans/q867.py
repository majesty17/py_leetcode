#!/usr/bin/python
# -*- coding:utf8 -*-

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """


        return zip(*A)