class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ""

        start, end = 0, 0  # track indices of the best palindrome found so far

        def expandAroundCenter(left: int, right: int) -> int:
            # Expand outward while characters match and indices are in bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # When loop ends, left/right have overshot by one on each side
            return right - left - 1  # length of the palindrome found

        for i in range(len(s)):
            len1 = expandAroundCenter(i, i)       # odd-length palindrome, center at i
            len2 = expandAroundCenter(i, i + 1)    # even-length palindrome, center between i and i+1
            max_len = max(len1, len2)

            # If we found a longer palindrome, update our start/end pointers
            if max_len > (end - start + 1):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]
        