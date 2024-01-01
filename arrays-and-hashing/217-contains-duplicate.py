# https://leetcode.com/problems/contains-duplicate/submissions/

from typing import List

# Naive solution with  set(list)
# Time complexity - O(n)
# Memory complecity - O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(nums)==len(set(nums))

# Optimal solution
# Time complexity - O(n)
# Memory complecity - O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new = set()
        for num in nums:
            if num in new:
                return True
            new.add(num)
        return False
