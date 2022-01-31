#!/usr/bin/python
# -*- coding:utf8 -*-


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace("IV", "+")
        s = s.replace("IX", "-")
        s = s.replace("XL", "*")
        s = s.replace("XC", "/")
        s = s.replace("CD", "(")
        s = s.replace("CM", ")")
        print s
        sum = 0
        for i in s:
            sum = sum + self.c2v(i)
        return sum

    def c2v(self, char):
        if char == "I":
            return 1
        if char == "V":
            return 5
        if char == "X":
            return 10
        if char == "L":
            return 50
        if char == "C":
            return 100
        if char == "D":
            return 500
        if char == "M":
            return 1000
        if char == "+":
            return 4
        if char == "-":
            return 9
        if char == "*":
            return 40
        if char == "/":
            return 90
        if char == "(":
            return 400
        if char == ")":
            return 900
