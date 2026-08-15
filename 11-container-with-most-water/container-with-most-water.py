class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        best = 0
        right = len(height) -1
        while left < right:
            h = min(height[left],height[right])
            width = right - left
            best = max(best,width*h)
            if height[left] < height[right]:
                left+=1
            else :
                right-=1
        return best


            
        