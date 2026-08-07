class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge case: if lengths differ, they can never be anagrams — exit early
        if len(s) != len(t):
            return False

        # Fixed-size array for 26 lowercase letters (a-z) — O(1) space since size is constant
        count = [0] * 26

        # Single pass: increment count for each char in s, decrement for each char in t
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1   # 'a' maps to index 0, 'b' to 1, ..., 'z' to 25
            count[ord(t[i]) - ord('a')] -= 1   # same index, but subtract for t

        # If s and t are true anagrams, every character's net count should be zero
        for c in count:
            if c != 0:
                return False

        return True

        return True 
    

  
   