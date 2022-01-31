#!/usr/bin/python
# -*- coding:utf8 -*-


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        sigh = +1 if x >= 0 else -1
        value = int(math.fabs(x))
        str_value = str(value)
        str_value = str_value[::-1]
        value = int(str_value) * sigh

        if value > 2147483647 or value < -2147483648:
            return 0

        return value
