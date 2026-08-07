class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        maxBlack = 0
        left = 0
        count = 0
        for right in range(len(blocks)):
            if blocks[right] == "B":
                count+=1
            if right >= k-1:
                maxBlack = max(maxBlack,count)
                if blocks[left] == "B":
                    count-=1
                left+=1
        return k-maxBlack
            

        