#!/usr/bin/python
# -*- coding:utf8 -*-


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        v=[]
        for i in words:
            v.append(self.w2m(i))
        return len(set(v))

    def w2m(self, words):
        a = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        ret = ""
        for i in words:
            ret = ret + a[ord(i) - 97]

        return ret
