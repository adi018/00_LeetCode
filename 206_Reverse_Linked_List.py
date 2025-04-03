
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        slow = None
        fast = head

        while fast:
            
            prev = slow
            slow = fast
            fast = fast.next
            slow.next = prev
        # end while

        return slow

        