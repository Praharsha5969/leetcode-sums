class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        csum = 0
        subcnt = 0
        seen = {0:1}
        for i in nums:
            csum+=i
            req = csum - k
            if req in seen :
                subcnt += seen[req]
            seen[csum] = seen.get(csum,0) + 1
        return subcnt


        