#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author： Smly
# @datetime： 2021/7/29 19:33 
# @Version： 1.0

def Hui(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            s = x
            xsum = 0
            i = 0
            n = len(str(x))
            while i < n:
                xsum += (x % 10) * 10 ** (n - 1)
                x = (x - (x % 10)) / 10
                n -= 1
            if s == xsum:
                return True
            else:
                return False


so = Solution()

print(so.isPalindrome(121))
