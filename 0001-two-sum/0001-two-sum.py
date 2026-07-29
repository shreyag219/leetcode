class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # value -> index, tracks numbers we've already visited
        
        for i, num in enumerate(nums):
            complement = target - num          # what value would complete the pair?
            if complement in seen:             # O(1) hash lookup
                return [seen[complement], i]   # found earlier index + current index
            seen[num] = i                      # record current number's index for future lookups
        
        return []  # no solution found (not expected per problem constraints)
        