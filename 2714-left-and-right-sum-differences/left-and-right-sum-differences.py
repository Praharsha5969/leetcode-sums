class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftsum = []
        rightsum = []
        lsum = 0
        rsum = 0
        for i in range(len(nums)):
            leftsum.append(lsum)
            lsum += nums[i]

        for i in range(len(nums)-1, -1, -1):
            rightsum.append(rsum)
            rsum += nums[i]

        rightsum.reverse()

        ans = []
        
        for i in range(0,len(nums)):
            ans.append(abs(leftsum[i]-rightsum[i]))
        return ans



            



        