from bisect import bisect_left, bisect_right
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first_position = bisect_left(nums,target)
        last_position = bisect_right(nums,target)
        if first_position == last_position :
            return [-1,-1]
        else :
            return [first_position,last_position-1]
        
        