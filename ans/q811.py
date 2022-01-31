#!/usr/bin/python
# -*- coding:utf8 -*-

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        a = {}

        for i in cpdomains:
            ct = i.split(" ")[0]
            ct=int(ct)
            url = i.split(" ")[1]
            sp = url.split(".")
            for j in range(len(sp)):
                suburl = ".".join(sp[j:])
                if a.has_key(suburl):
                    a[suburl]=a[suburl]+ct
                else:
                    a[suburl]=ct
        ret=[]
        for i in a:
            ret.append("%d %s" % (a[i],i))
        return ret