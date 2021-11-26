class Solution:
    def longestValidParentheses(self, s: str) -> int:
        queue = [0]
        longest = 0
        for c in s:
            if c == "(":
                queue.append(0)
            else:
                if len(queue) > 1:
                    val = queue.pop()
                    queue[-1] += val + 2
                    longest = max(longest, queue[-1])
                else:
                    queue = [0]
        return longest

