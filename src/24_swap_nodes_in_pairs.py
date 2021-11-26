from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(0, head)
        cur = head
        if head is None or head.next is None:
            return head
        while cur and cur.next:
            temp = cur.next
            if temp:
                cur.next = temp.next
                temp.next = cur
                prev.next = temp
                prev = cur
                cur = cur.next
        return dummy.next

if __name__ == "__main__":
    a = ListNode(4)
    b = ListNode(3, a)
    c = ListNode(2, b)
    e = ListNode(1, c)
    assert Solution().swapPairs(e)