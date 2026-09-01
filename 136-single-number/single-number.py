class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        for key,values in freq.items():
            if values == 1:
                return key
            

        