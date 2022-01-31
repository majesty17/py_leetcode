#!/usr/bin/python
# -*- coding:utf8 -*-


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ret=[]
        for i in words:
            if self.isLine(i):
                ret.append(i)
        return ret

    def isLine(self,word):
        word=word.lower()
        heat=self.numofLetter(word[0])
        for i in word[1:]:
            if self.numofLetter(i)!=heat:
                return False
        return True
    def numofLetter(self,let):
        if let in "qwertyuiop":
            return 1
        if let in "asdfghjkl":
            return 2
        if let in "zxcvbnm":
            return 3
        return -1


