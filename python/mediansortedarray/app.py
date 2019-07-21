# ******************************************
#  Author : Ali Azhari 
#  Created On : Sat Jul 20 2019
#  File : app.py
# *******************************************/

class Solution(object):
    def findMedianSortedArrays1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        length1 = len(nums1)
        length2 = len(nums2)
        i = j = 0
        while i < length1 and j < length2:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        if nums1[i] < nums2[j]:
            nums.append(nums1[i])
            i += 1

    # Using binary search tree. This takes O(log(min(length of nums, length of nums2)))
    def findMedianSortedArrays2(self, nums1, nums2):

        length1, length2 = len(nums1), len(nums2)

        if length1 > length2:
            nums1, nums2, length1, length2 = nums2, nums1, length2, length1

        if length2 == 0:
            raise ValueError

        first, last, half_len = 0, length1, (length1 + length2 + 1) // 2
        while first <= last:
            i = (first + last) // 2
            j = half_len - i
            if i < length1 and nums2[j - 1] > nums1[i]:
                # i is too small, must increase it
                first = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i is too big, must decrease it
                last = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                if (length1 + length2) % 2 == 1:
                    return max_of_left

                if i == length1: min_of_right = nums2[j]
                elif j == length2: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2.0
                

        

        
solution = Solution()
print(solution.findMedianSortedArrays2([1, 2], [3, 4]))