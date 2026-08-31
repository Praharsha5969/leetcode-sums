class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d1 = {}
        d2 = {}
        for i in ransomNote:
            d1[i] = d1.get(i,0)+1
        for i in magazine:
            d2[i] = d2.get(i,0)+1
        for key in d1:
            if d1[key] > d2.get(key, 0):
                return False

        return True

















        