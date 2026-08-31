class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = {}
        for i in arr:
            freq[i] = freq.get(i,0)+1
        occurrences = set()

        for i in freq.values():
            if i in occurrences:
                return False
            occurrences.add(i)

        return True

        
        