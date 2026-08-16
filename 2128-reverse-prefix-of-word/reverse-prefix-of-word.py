class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        for i in range(len(word)):
            if word[i] == ch:
                text = word[0:i+1]
                coll = word[i+1:len(word)]
                word = text[::-1]+coll
                break
        return word
        