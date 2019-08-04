# ******************************************
#  Author : Ali Azhari
#  Created On : Fri Jul 26 2019
#  File : app.py
# *******************************************/

import sys


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == '':
            return 0
        i = 0
        sign = 1
        length = len(str)
        while str[i] == ' ' and i < length - 1:
            i += 1
        if i == length:
            return 0

        if str[i] == '-':
            sign = -1
            i += 1
        elif str[i] == '+':
            i += 1
        num = 0

        while i < length:
            try:
                num = num * 10 + int(str[i])
                i += 1
            except:
                break
        max = pow(2, 31) - 1
        min = pow(-2, 31)
        num = num * sign
       
        if num > max:
            return max
        elif num < min:
            return min
        return num


solution = Solution()
print(solution.myAtoi(' '))
