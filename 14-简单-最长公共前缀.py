#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author： Smly
# @datetime： 2021/8/1 8:06 
# @Version： 1.0

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    """
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""
    思路：
    :param strs:strings list
    :return: public prefix
    """
    s = ''
    if len(strs) == 0:
        return s
    for str_ in zip(*strs):
        print(str_)
        print(type(str_))
        print(set(str_))
        if len(set(str_)) == 1:
            s += str_[0]
            print(s)
        else:
            break
    return s


print(longestCommonPrefix([""]))
