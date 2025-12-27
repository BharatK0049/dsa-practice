# Problem: Two Sum
LeetCode #1

## Pattern
Existence via hashing

## Problem Restatement
I am given an array of integers and a target number whose sum I should get from two numbers in the array. It is assumed that there is only one solution and the same number (if only in the same index) cannot be used twice.

## Initial Thoughts (Before Coding)
- I can look at every possible pair and see if it adds upto the target
- A nested loop to look at every other j value while i is fixed at leftmost
- How can I make this lesser than O(n^2)

## Failed Attempts / Confusions
- Nested loop takes a lot of time, leads to unnecessary checks.
- Tried to see if checking for a value whose target - value existed in the array, but that would often check the same number itself which violates the second rule.
- Tried to map indices to values to see if the number in the same index is being checked again or not, still violates rule 2
- I think when using brute force, when we pick one value of the pair, say 'i', j is the target - i that we keep trying to see if it equals to which is what is time consuming and redundant and rather than looking at every possible combination, we are just checking to see if target - i existed in the loop in the first place to begin with.
- Property: What the ultimate takeaway from this is to remember previously seen values to avoid repeated scanning.

## Final Approach (In Words)
- I first loop through the array from i ranging from 0 to n-1
- for every number ith index, I check to see if I have already seen the complement i.e. value - num[i] in the array rather than checking for every number to be value - num[i]
- I add the value: index pair of i in the hashmap (dictionary) and proceed to move on to the next one
- If I found an ith value whose target - num[i] is in the hashmap, then I can just use the hashmap to fetch that index along with the current ith index I have.

## Code
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = {}

        for i in range(len(nums)):
            if target - nums[i] not in seen_numbers:
                seen_numbers[nums[i]] = i
            else:
                return [i, seen_numbers[target-nums[i]]]

