#!/usr/bin/python
# -*- coding:utf8 -*-
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        if length == 1:
            return nums[0]

        nums.sort()
        i = 0
        while True:
            if i+1 > length - 1:
                return nums[-1]


            if nums[i] != nums[i + 1]:
                return nums[i]
            i = i + 2

