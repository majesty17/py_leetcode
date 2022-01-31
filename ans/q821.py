#!/usr/bin/python
# -*- coding:utf8 -*-



class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """

        ind = [a for a in range(len(S)) if S[a] == C]
        # return ind
        import math
        ret = [0] * len(S)
        for i in range(len(S)):
            dis=[ int(math.fabs(a-i)) for a in ind ]
            ret[i]=min(dis)
        return ret
