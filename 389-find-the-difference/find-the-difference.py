class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        freq = {}

        
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        
        for char in t:
            if char not in freq:
                return char

            freq[char] -= 1

            if freq[char] < 0:
                return char

        