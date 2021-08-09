#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author： Smly
# @datetime： 2021/8/8 20:37 
# @Version： 1.0
from typing import List

"""
# 1. sorted内置函数法
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.append(i**2)
        return sorted(ans)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        m = 0
        while m <= n-1:
            i = nums[m]*nums[m]
            j = nums[n-1]*nums[n-1]
            if i >= j:
                ans.append(i)
                m += 1
            else:
                ans.append(j)
                n -= 1
        return ans[::-1]
# 2. 双指针法
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        m = 0
        while m <= n-1:
            i = nums[m]*nums[m]
            j = nums[n-1]*nums[n-1]
            if i >= j:
                ans.append(i)
                m += 1
            else:
                ans.append(j)
                n -= 1
        return ans[::-1]
so = Solution()
print(so.sortedSquares([-4,-1,0,3,10]))
"""
