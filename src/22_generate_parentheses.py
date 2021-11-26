from typing import List, Optional

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def generate(p, left, right, res=[]):
            if left:
                generate(p + '(', left - 1, right, res)
            if right > left:
                generate(p + ')', left, right - 1, res)
            if right == 0:
                res.append(p)
            return res
        return generate('', n, n, [])

