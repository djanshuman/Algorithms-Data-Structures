class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        resLen = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            resLen = max(resLen, r - l + 1)

        return resLen


if __name__ == "__main__":
    s = "abcabcbb"
    obj = Solution()
    print(obj.lengthOfLongestSubstring(s, ))
