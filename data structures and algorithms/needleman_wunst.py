# String comparision using dynamic programming

def delta(char1, char2):
    '''Mismatch function'''
    if char1 == char2:
        return 0
    else:
        return 1

def dyn_need(str1, str2):
    '''Algorithm to match two strings'''
    if len(str1) == 0 or len(str2) == 0:
        return max(len(str1), len(str2))
    return min(dyn_need(str1[:-1], str2[:-1]) + delta(str1[-1], str2[-1]),
               dyn_need(str1, str2[:-1]) + 1,
               dyn_need(str1[:-1], str2) + 1)
print(dyn_need('boyasa', 'manasa'))
