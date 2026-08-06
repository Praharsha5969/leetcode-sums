class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowelCount = 0
        left = 0
        maxVowelcount = 0
        for right in range(len(s)):
            if s[right] in "aeiou":
                vowelCount+=1
            if right >= k-1:
                maxVowelcount = max(maxVowelcount,vowelCount)
                if s[left] in "aeiou":
                    vowelCount-=1
                left+=1
        return maxVowelcount




        
        