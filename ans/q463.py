#!/usr/bin/python
# -*- coding:utf8 -*-

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        h = len(grid)
        w = len(grid[0])
        for i in range(h):
            for j in range(w):
                if grid[i][j] != 1:
                    continue
                delta = 4
                if i < h - 1 and grid[i + 1][j] == 1:
                    delta = delta - 1
                if i > 0 and grid[i - 1][j] == 1:
                    delta = delta - 1
                if j > 0 and grid[i][j - 1] == 1:
                    delta = delta - 1
                if j < w - 1 and grid[i][j + 1] == 1:
                    delta = delta - 1
                ret = ret + delta
        return ret
