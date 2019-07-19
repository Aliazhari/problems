# ******************************************
#  Author : Ali Azhari 
#  Created On : Fri Jul 19 2019
#  File : app.py
# *******************************************/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
       
        l3 = None
        current = None
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            sum = val1 + val2 + carry
            # carry = sum // 10
            # sum = sum % 10
            carry, sum = divmod(sum, 10)  
            temp = ListNode(sum)
    
            if l3 is None:
                l3 = temp
                current = l3
            else:
                current.next = temp
                current = current.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
       
            
        return l3