#!/usr/bin/python
# -*- coding:utf8 -*-
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # import numpy as np
        # data = np.array(grid)
        #
        # max0 = data.max(axis=0)
        # max1 = data.max(axis=1)
        max1 = []
        for i in grid:
            max1.append(max(i))
        max0 = []
        t_grid = zip(*grid)
        for i in t_grid:
            max0.append(max(i))

        sum = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print data[i][j]
                sum = sum + (min(max0[j], max1[i]) - grid[i][j])

        return sum  # [max0, max1]
