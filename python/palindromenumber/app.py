# ******************************************
#  Author : Ali Azhari 
#  Created On : Sun Aug 04 2019
#  File : app.py
# *******************************************/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0: return False

        num = x
        reverse = 0

        while num != 0:
            remainder = num % 10
            reverse = reverse * 10 + remainder
            num = num // 10

        return x == reverse

solution = Solution()
print(solution.isPalindrome(123))
print(solution.isPalindrome(-121))







