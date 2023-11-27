from typing import Optional
from sys import maxsize
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            # 反轉串列
            temp = slow.next 
            slow.next = prev
            prev = slow
            slow = temp

        maxi = -maxsize
        while slow:
            maxi = max(maxi, slow.val + prev.val)
            slow = slow.next
            prev = prev.next
        return maxi