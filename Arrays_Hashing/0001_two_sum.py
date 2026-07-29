"""
Problem: Two Sum
LeetCode: #1
Difficulty: Easy

Approach:
Use a hash map (dictionary) to store numbers we've already seen.
For each number, calculate the complement (target - current number).
If the complement exists in the hash map, we've found the answer.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i