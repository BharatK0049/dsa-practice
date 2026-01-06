# Problem: Remove Duplicates from Sorted Array
LeetCode #27

## Pattern
Two-pointers

## Problem Restatement
I have an array which is sorted but there exist some duplicate values. The goal is to remove them in-place (meaning you shouldn't use an additional array to remove them), but the key idea is to have the unique elements at the beginning of the array and it doesn't matter what comes later.

## Initial Thoughts (Before Coding)
- Use an extra array and try to get the unique elements alone 
- 
- 

## Failed Attempts / Confusions
- (I didn't even try to solve this one chief, dived right into the answer because I solved it back in June 2025)
- Returning only the unique count doesn't solve the problem as an internal judge code checks to see if the code has been sorted in place

## Final Approach (In Words)
- keep track of right pointer from 1 and keep iterating it till length of array.
- skip element where r-1 value is equal to r,
- otherwise move arr[l] to arr[r] and increment l by 1
- Return l as the count of unique elements 

## Code
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r-1] == nums[r]:
                continue
            else:
                nums[l] = nums[r]
                l += 1
        
        return l
```

## Key Insights
- Array must be sorted as well as the unique count must be returned.
- When the element one less than the right pointer is not equal to that of the right pointer, then there is a unique value, so we count that and move left to where the right currently is.
- Each time the left increases is also the number of unique elements in the array.
