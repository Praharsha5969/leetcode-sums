class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        if n < 1000:
            return 0
        else :
            for i in range(1000,n+1):
                count+=1
        return count
        