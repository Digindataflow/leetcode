from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, o: object) -> bool:
        return self.val == o.val and self.next == o.next

    def __lt__(self, o: object) -> bool:
        return self.val < o.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode(0)
        queue = []
        count = 0
        for node in lists:
            if node:
                count += 1
                heapq.heappush(queue, (node.val, count, node))

        while len(queue) > 0:
            _, _, cur.next = heapq.heappop(queue)
            if cur.next.next:
                count += 1
                heapq.heappush(queue, (cur.next.next.val, count, cur.next.next))
            cur = cur.next

        return dummy.next

if __name__ == "__main__":
    a = ListNode(5)
    b = ListNode(4, a)
    c = ListNode(1, b)
    d = ListNode(4)
    e = ListNode(3, d)
    f = ListNode(1, e)
    g = ListNode(6)
    h = ListNode(2, g)
    c < b
    assert Solution().mergeKLists([c, f, h])