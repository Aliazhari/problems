# ******************************************
#  Author : Ali Azhari 
#  Created On : Tue Aug 06 2019
#  File : app.py
# *******************************************/

class Solution(object):
    # Brute force  time complexity is n**2
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        print(length)
        i = 0
        area = 0
        while i < length - 1:
            j = i + 1
            while j < length :
                w = j - i
                l = min(height[i], height[j])
                area = max(area, w * l)
                print(height[i], height[j], area)
                j += 1
            i += 1
        return area

    # Using two pointers algorithm, time complexity is O(n)
    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        area = 0

        while left < right:
            area = max(area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else: right -= 1

        return area

solution = Solution()
print(solution.maxArea1([1,8,6,2,5,4,8,3,7]))


        