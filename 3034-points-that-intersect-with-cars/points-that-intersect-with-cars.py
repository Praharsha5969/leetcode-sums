class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        points = {}
        for start,end in nums:
            for i in range(start,end+1):
                points[i] = 1
        return len(points)

        
        