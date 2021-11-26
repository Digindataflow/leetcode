from typing import List, Optional
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for item in strs:
            mapping[tuple(sorted(item))].append(item)
        return list(mapping.values())
