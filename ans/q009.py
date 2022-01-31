#!/usr/bin/python
# -*- coding:utf8 -*-


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        st = str(x)

        if st[::-1] == st:
            return True
        return False
