#!/usr/bin/python
# -*- coding:utf8 -*-


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        sign = 1 if num >= 0 else -1

        bin_num = bin(num).replace("0b", "").replace("-", "")

        num_list = []
        for i in bin_num:
            num_list.append("0" if i == "1" else "1")
        num_str = "".join(num_list)

        return int(num_str, 2) * sign
