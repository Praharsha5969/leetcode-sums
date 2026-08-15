class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxcustomer = 0
        csum = 0
        for row in accounts:
            csum = sum(row)
            maxcustomer = max(csum,maxcustomer)
        return maxcustomer


        
        