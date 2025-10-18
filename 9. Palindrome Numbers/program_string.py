class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return False
        temp = str(x)
        x_split = list(temp)
        i = 0
        j = len(x_split)-1
        while i < j:
            if x_split[i] != x_split[j]: return False
            i += 1
            j -= 1
        return True