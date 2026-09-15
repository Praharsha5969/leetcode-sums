class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        sum_digits = 0
        while n > 0:
            sum_digits+=n%k
            n//=k
        return sum_digits

        