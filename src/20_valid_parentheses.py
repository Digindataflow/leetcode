from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        left = '([{'
        right = ')]}'
        stack = deque()

        for i, item in enumerate(s):
            if item in left:
                stack.append(item)
            else:
                if len(stack) == 0 or left[right.index(item)] != stack.pop():
                    return False
        return stack.__len__() == 0