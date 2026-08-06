class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        left = 0
        currentsum = 0
        count = 0
        for right in range(len(arr)):
            currentsum+=arr[right]
            if right >= k-1:
                avg = currentsum / k
                if avg >= threshold:
                    count+=1
                currentsum-=arr[left]
                left+=1
        return count
            

        