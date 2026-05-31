# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1: return list2
        if not list2: return list1

        dummy = ListNode(-1)  
        ret = dummy

        firstCurr = list1
        secondCurr = list2

        while firstCurr and secondCurr:
            if firstCurr.val <= secondCurr.val:
                ret.next = firstCurr
                firstCurr = firstCurr.next   
            else:
                ret.next = secondCurr
                secondCurr = secondCurr.next 
            ret = ret.next

        ret.next = firstCurr if firstCurr else secondCurr

        return dummy.next
