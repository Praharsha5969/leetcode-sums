class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        res = []
        while k > 0 :
            max_key = 0
            
            max_key = max(freq, key=freq.get)
            res.append(max_key)
            freq.pop(max_key)
            k-=1
        return res



        