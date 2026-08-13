class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(i.lower() for i in s if i.isalnum())
        left = 0
        right = len(cleaned)-1
        flag = 0
        while left < right:
            if cleaned[left] == cleaned[right]:
                left+=1
                right-=1
            else :
                flag = 1
                break
        return flag == 0

        