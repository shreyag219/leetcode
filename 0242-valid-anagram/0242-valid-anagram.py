class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams must have the same length by definition
        if len(s) != len(t):
            return False
        
        count = {}
        
        # Increment count for every character in s
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Decrement count for every character in t
        for char in t:
            count[char] = count.get(char, 0) - 1
        
        # If s and t are true anagrams, every count cancels out to zero
        return all(v == 0 for v in count.values())
        