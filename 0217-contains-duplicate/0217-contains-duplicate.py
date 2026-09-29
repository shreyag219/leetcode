class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        
        for num in nums:
            if num in seen:      # O(1) average lookup
                return True      # early exit
            seen.add(num)        # remember this value
        
        return False