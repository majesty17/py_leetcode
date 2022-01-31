#!/usr/bin/python
# -*- coding:utf8 -*-

#ps 这题最好的办法应该是先排序，然后两头往中间凑，然而需要下标。。

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
