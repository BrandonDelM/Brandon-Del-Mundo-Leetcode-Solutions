class Solution(object):
    def romanToInt(self, s):
        letters = list(s)
        n = 0
        for i in range(len(letters)):
            check = n
            current_letter = letters[i]
            if i+1 != len(letters):
                next_letter = letters[i+1]
                if next_letter == 'D' or next_letter == 'M':
                    if current_letter == 'C':
                        n -= 100
                if next_letter == 'L' or next_letter == 'C':
                    if current_letter == 'X':
                        n -= 10
                if next_letter == 'V' or next_letter == 'X':
                    if current_letter == 'I':
                        n -= 1
            if n == check:
                if current_letter == 'M':
                    n += 1000
                elif current_letter == 'D':
                    n += 500
                elif current_letter == 'C':
                    n += 100
                elif current_letter == 'L':
                    n += 50
                elif current_letter == 'X':
                    n += 10
                elif current_letter == 'V':
                    n += 5
                else:
                    n += 1
        return n