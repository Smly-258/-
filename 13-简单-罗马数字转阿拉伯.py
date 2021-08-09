#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author： Smly
# @datetime： 2021/8/4 21:25 
# @Version： 1.0


class Solution:
    def romanToInt(self, s):
        """
        罗马数字转阿拉伯
        :param s:代表罗马数字的字符串
        :return:返回罗马数字转为阿拉伯数字的值
        """
        # 使用字典收录罗马数字的值
        num_dir = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # 记录最后值用
        ans = 0
        for i in range(len(s)):
            # 注意这里不能直接遍历字符串
            if i < len(s) - 1 and num_dir[s[i]] < num_dir[s[i + 1]]:
                ans -= num_dir[s[i]]
            else:
                ans += num_dir[s[i]]
        return ans
