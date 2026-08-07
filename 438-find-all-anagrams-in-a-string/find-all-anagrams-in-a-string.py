class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        output = []
        d1 = {}
        d2 = {}
        left = 0
        for i in p :
            d2[i] = d2.get(i,0) + 1
        
        for right in range(len(s)):
            d1[s[right]] = d1.get(s[right],0) + 1
            if right >= len(p) - 1:
                if d1 == d2 :
                    output.append(left)
                d1[s[left]]-=1
                if d1[s[left]] == 0:
                    d1.pop(s[left])
                left+=1
        return output
                

        