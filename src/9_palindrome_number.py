class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x = str(x)

        i = 0
        j = len(x) - 1
        while i <= j:
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__ == "__main__":
    sample = [121, 1234, 1231, -816]
    for item in sample:
        print(Solution().isPalindrome(item))
