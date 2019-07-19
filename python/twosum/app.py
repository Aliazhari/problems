# ******************************************
#  Author : Ali Azhari 
#  Created On : Thu Jul 18 2019
#  File : app.py
# *******************************************/

import time
import datetime

# first solution. it takes O(n**2)
class Solution(object):
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

    # second solution. it takes O(n)
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement = {}
        complement[target - nums[0]] = 0
        for i in range(1, len(nums) ):
            if nums[i] in complement:
                return [complement[nums[i]], i]
            else:
                complement[target - nums[i]] = i
        return None

# flag = 10000000
# t1 = time.time()   

start = datetime.datetime.now()
solution1 = Solution()
print(solution1.twoSum1([2, 7, 3, 8, 5,], 9))
end = datetime.datetime.now()
elapsed = end - start 
print('elapsed time fo solution 1 is: ')
print(elapsed)

# t2 = time.time()

start = datetime.datetime.now()
solution2 = Solution()
print(solution2.twoSum2([2, 7, 3, 8, 5,], 9))
end = datetime.datetime.now()
elapsed = end - start 
print('elapsed time fo solution 2 is: ')
print(elapsed )