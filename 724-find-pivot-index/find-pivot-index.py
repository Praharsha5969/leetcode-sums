class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefixSum = [0]
        s = 0
        for i in range(len(nums)):
            s+=nums[i]
            prefixSum.append(s)
        flag = 0
        for i in range(len(nums)):
            leftsum = prefixSum[i]
            rightsum = prefixSum[len(nums)] - prefixSum[i+1]
            if leftsum == rightsum:
                return i
                flag = 1
            
                
        if flag == 0:
            return -1


        