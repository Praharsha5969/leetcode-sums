class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = []
        for i in range(n):
            digit = start + 2 * i
            nums.append(digit)
        res = 0
        for i in range(n):
            res ^= nums[i]
        return res