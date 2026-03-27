'''
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        # define ascii window for all a-z alphabets
        # initialize length and variables
        check_window = [0] * 26
        window = [0] * 26
        len_check = len(p)
        len_original = len(s)
        a = ord('a')
        res = []

        # one-time window initialization and mark first result if true
        for i in range(len_check):
            check_window[ord(p[i]) - a] += 1
            window[ord(s[i]) - a] += 1
        if check_window == window:
            res.append(0)

        # Now traverse sliding window , by adding one char right and remove 1 char left 

        for i in range(len_check,len_original):
            window[ord(s[i - len_check]) - a] -= 1
            window[ord(s[i]) - a] += 1

            if check_window == window:
                res.append( i - len_check +1)
        return res


'''
More performant way '''

def find_all_anagrams(original: str, check: str) -> list[int]:
    if len(original) < len(check):
        return []

    # 1. Map out the target frequencies
    check_counter = {}
    for c in check:
        check_counter[c] = check_counter.get(c, 0) + 1
        
    # 2. 'required' is the number of UNIQUE characters to satisfy
    required = len(check_counter)
    formed = 0
    left = 0
    window = {}
    res = []

    # 3. Iterate over the ORIGINAL string
    for right in range(len(original)):
        right_char = original[right]
        window[right_char] = window.get(right_char, 0) + 1

        # Check if this character now meets the required frequency
        if right_char in check_counter and window[right_char] == check_counter[right_char]:
            formed += 1 

        # 4. Maintain the window size
        if right >= len(check):
            out_char = original[left]
            
            # If the char leaving was previously satisfying the count, decrement formed
            if out_char in check_counter and window[out_char] == check_counter[out_char]:
                formed -= 1

            window[out_char] -= 1
            left += 1

        # 5. Record result if all unique characters are satisfied
        if formed == required:
            res.append(left)
            
    return res
