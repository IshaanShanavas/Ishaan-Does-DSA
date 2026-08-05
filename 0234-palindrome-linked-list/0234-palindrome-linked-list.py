# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        check = []
        while head is not None:
            check.append(head.val)
            head = head.next
        
        if check == check[::-1]:
            return True
        else:
            return False

        