class Solution:
    def myPow(self, x: float, n: int) -> float:
        n_neg = n < 0
        res = self._my_pow(x, abs(n))
        return 1/res if n_neg else res

    def _my_pow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x

        n, remainder = divmod(n, 2)
        temp = self._my_pow(x, n)
        return temp * temp if remainder == 0 else temp * temp * x