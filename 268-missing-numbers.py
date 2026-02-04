class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = set(nums)
        for i in range(len(h)):
            if i not in h:
                return i
        return len(h)
