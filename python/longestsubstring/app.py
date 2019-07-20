# ******************************************
#  Author : Ali Azhari
#  Created On : Fri Jul 19 2019
#  File : app.py
# *******************************************/


class Solution(object):

    # Brute force that takes O(n**2)
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        # for index, i in enumerate(s):
        #     print(index, i)

        length = len(s)
        
        answer = 0
        count = 0
        for i in range(0, length):
            count = 0
            j = i
            str= []
           
            while j < length and s[j] not in str:
                
                str.append(s[j])
                count += 1
                j += 1
            answer = max(answer, count)
                   
        return answer
                    
            
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicts = {}

        x = dicts['hello'] + 1
        print(x)




solution = Solution()
solution.lengthOfLongestSubstring2('hello')
