class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        for key,value in freq.items():
            if value > len(nums)//2:
                return key
        
        