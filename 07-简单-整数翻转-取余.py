#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author： Smly
# @datetime： 2021/7/24 18:09 
# @Version： 1.0
class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        """
        取余从后一个一个拿数
        :param x: 被翻转的数
        :return: 翻转完成的数
        """
        i = 0
        if x < 0:
            x = -x
            xsum = 0
            n = len(str(x))
            while i < n:
                xsum += (x % 10) * 10 ** (n - 1)
                x = (x - (x % 10)) / 10
                n -= 1
            if -2 ** 31 <= xsum <= 2 ** 31 - 1:
                return int(xsum) * -1
            else:
                return 0
        elif x > 0:
            xsum = 0
            n = len(str(x))
            while i < n:
                xsum += (x % 10) * 10 ** (n - 1)
                x = (x - (x % 10)) / 10
                n -= 1
            if -2 ** 31 <= xsum <= 2 ** 31 - 1:
                return int(xsum)
            else:
                return 0
        else:
            return 0
