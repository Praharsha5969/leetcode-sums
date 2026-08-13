class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        vowels = set("aeiouAEIOU")
        a = list(s)
        right = len(a) - 1
        while left < right:
            while left < right and a[left] not in vowels:
                left+=1
            while left < right and a[right] not in vowels:
                right-=1
            a[left],a[right] = a[right],a[left]
            left+=1
            right-=1
        return ''.join(a)
        