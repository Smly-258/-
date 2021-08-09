#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author： Smly
# @datetime： 2021/7/29 16:56 
# @Version： 1.0
"""
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出
和为目标值 target 的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return [i, j]


print(twoSum([3, 1, 3], 6))
