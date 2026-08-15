class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst=list(s)
        left = 0
        right = len(lst)-1
        while left < right:
            if lst[left].isalpha() and lst[right].isalpha() :
                lst[left],lst[right]=lst[right],lst[left]
                left+=1
                right-=1
            elif not lst[left].isalpha():
                left+=1
            else :
                right-=1
            
                

        return ''.join(lst)

        