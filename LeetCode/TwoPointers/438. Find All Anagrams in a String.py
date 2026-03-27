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
    # 1. Edge case: If the string to check is longer than the original, no anagrams possible
    if len(original) < len(check):
        return []

    # 2. Map out the target frequencies (The "Goal")
    check_counter = dict()
    for c in check:
        check_counter[c] = check_counter.get(c, 0) + 1
        
    # 3. Initialize State Variables
    # 'required' is the number of UNIQUE characters that must reach a specific frequency
    required = len(check_counter)
    formed = 0
    left = 0
    window = dict()
    res = []

    # 4. Iterate over the ORIGINAL string with the 'right' pointer
    for right in range(len(original)):
        # Expand: Add character from the right to our current window
        right_char = original[right]
        window[right_char] = window.get(right_char, 0) + 1

        # If this character's count in our window matches the target count exactly, 
        # we've satisfied one unique character requirement.
        if right_char in check_counter and window[right_char] == check_counter[right_char]:
            formed += 1 

        # 5. Maintain Window Size: If window exceeds len(check), slide 'left' forward
        if right >= len(check):
            out_char = original[left]
            
            # If the character leaving was currently satisfying a frequency requirement,
            # we must decrement 'formed' before we reduce its count.
            if out_char in check_counter and window[out_char] == check_counter[out_char]:
                formed -= 1

            window[out_char] -= 1
            
            # Memory Cleanup: Remove the key if the count hits zero
            if window[out_char] == 0:
                del window[out_char]
                
            left += 1

        # 6. Success Check: If all unique character requirements are met, we found an anagram
        if formed == required:
            res.append(left)
            
    return res

# --- Execution Block ---
if __name__ == "__main__":
    # Example Input: 
    # original: cbaebabacd
    # check: abc
    original = input().strip()
    check = input().strip()
    res = find_all_anagrams(original, check)
    print(" ".join(map(str, res)))

