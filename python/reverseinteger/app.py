# ******************************************
#  Author : Ali Azhari 
#  Created On : Tue Jul 23 2019
#  File : app.py
# *******************************************/
import sys
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        
            return 0
        if x < 0: sign = -1
        else: sign = 1
        
        x = x * sign

        num = 0

        str1 = str(x)
        coef = pow(10, len(str1) - 1)

        while x != 0:
            remainder = x % 10
            num += (remainder * coef)
            if num > 2**31 - 1 or num < 2**31: return 0
            coef //= 10
            x //= 10
        
        num *= sign
        return num

solution = Solution()
print(solution.reverse(1534236469))
