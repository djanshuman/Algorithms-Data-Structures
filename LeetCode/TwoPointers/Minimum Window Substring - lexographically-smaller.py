'''
Minimum Window Substring
Given two strings, original and check, return the shortest substring of original that contains every character in check, including duplicates. If multiple valid substrings have the same length, return the lexicographically smallest one.

Parameters

original: The source string.
check: The required characters.
Result

The minimum valid window in original.
Examples

Example 1

Input: original = "cdbaebaecd", check = "abc"

Output: baec

Explanation: Both cdba and baec are valid windows of length 4. We return baec because it is lexicographically smaller.

Constraints

1 <= len(check), len(original) <= 10^5
original and check contain only uppercase and lowercase English letters. Characters are case-sensitive.
'''

def get_minimum_window(original: str, check: str) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    need = dict()

    for c in check:
        need[c] = need.get(c,0) + 1

    have = dict()
    found  = 0
    left = 0
    satisfied = len(need)
    min_len = float("inf")
    min_window = ""


    for right in range(len(original)):
        # 1. Expand window by adding original[right]
        ele = original[right]
        have[ele] = have.get(ele,0) + 1

        if ele in need and have[ele] == need[ele]:
            found += 1
            
        # 2. Shrink from left while window is valid
        while found == satisfied:
            curr_len = right - left + 1
            curr_window = original[left:right+1]
            
            # Update best: prefer shorter, then lexicographically smaller | if smaller len found then go-ahead other if similar found then 
            # check if curr window lexographically smaller then previous found
            if (curr_len < min_len or (curr_len == min_len and curr_window < min_window)):
                min_len = curr_len
                min_window = curr_window

            # Remove original[left] from window
            left_ele = original[left]
            have[left_ele] -=1

            if left_ele in need and have[left_ele] < need[left_ele]:
                found -=1
            left += 1


    return min_window
        

if __name__ == "__main__":
    original = input()
    check = input()
    res = get_minimum_window(original, check)
    print(res)
