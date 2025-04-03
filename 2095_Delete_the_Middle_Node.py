# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
            
        fast = head
        slow = head
        prev = None

        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                prev = slow
                slow = slow.next
            # end if
        # end while

        if prev:
            prev.next = slow.next
        # end if

        return head

        