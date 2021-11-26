from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        shortest = min(strs, key=len)
        for i, item in enumerate(shortest):
            for other in strs:
                if item != other[i]:
                    return shortest[:i]
        return shortest