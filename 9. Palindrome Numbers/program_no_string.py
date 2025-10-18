class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return False
        n = 1
        while n*10 <= x:
            n *= 10
        i = n
        j = 1
        while j < i:
            if (x/i)%10 != (x/j)%10:
                return False
            i /= 10
            j *= 10
        return True