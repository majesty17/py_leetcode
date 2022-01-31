#!/usr/bin/python
# -*- coding:utf8 -*-

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num

        ret = 0
        while True:
            ret += num % 10
            num = int(num / 10)

            if num == 0:
                break

        return self.addDigits(ret)
