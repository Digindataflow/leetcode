
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        mapping = {}
        index = 0
        while curr:
            mapping[index] = curr
            curr = curr.next
            index += 1

        rm_index = len(mapping) - n
        if rm_index == 0:
            return head.next
        elif n == 1:
            mapping.get(rm_index-1).next = None
            return head
        else:
            mapping.get(rm_index-1).next = mapping.get(rm_index+1)
            return head

