#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author： Smly
# @datetime： 2021/7/24 18:06
# @Version： 1.0

class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        """
        转为字符串翻转
        :param x: 被翻转的数
        :return: 翻转完成的数
        """
        if x < 0:
            x = -x
            s = str(x)[::-1]
            ends = -1 * int(s)
        elif x > 0:
            ends = int(str(x)[::-1])
        else:
            ends = 0
        if -2 ** 31 <= ends <= 2 ** 31 - 1:
            return ends
        else:

            return 0
