# ******************************************
#  Author : Ali Azhari 
#  Created On : Sun Jul 21 2019
#  File : app.py
# *******************************************/

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) < 1: return ''
        
        first = last = 0
        length = len(s)
        for i in range(0, length):
            length = max(self.expandCenter(s, i, i), self.expandCenter(s, i, i + 1))
            if length > (last - first):
                first = i - (length - 1) // 2
                last = i + length //2

        return s[first:(last + 1)]

    def expandCenter(self, s, left, right):
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1


solution = Solution()


print(solution.longestPalindrome('abaccaba'))