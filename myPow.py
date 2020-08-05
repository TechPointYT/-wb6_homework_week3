class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not x:
            return 0
        if n == 0:
            return 1
        elif n < 0:
            return  self.myPow(1/x, -1*n)
        elif n%2:
            return x*self.myPow(x, n-1)
        return self.myPow(x*x, n//2)
