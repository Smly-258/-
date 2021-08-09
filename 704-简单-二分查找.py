#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author： Smly
# @datetime： 2021/8/5 10:54 
# @Version： 1.0
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target
        写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1
        难度：**简单**
        :param nums:
        :param target:
        :return:
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if target > nums[mid]:
                start = mid + 1
            else:
                end = mid
        return start
