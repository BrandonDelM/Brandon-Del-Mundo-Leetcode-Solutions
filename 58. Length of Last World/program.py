class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.strip().split()[len(s.strip().split())-1])