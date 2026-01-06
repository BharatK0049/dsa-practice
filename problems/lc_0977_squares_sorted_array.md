# Problem: Squares of a Sorted Array
LeetCode #977

## Pattern
Two Pointers

## Problem Restatement
Given a sorted array (possibly containing negative numbers), return a new array containing the squares of each number, sorted in non-decreasing order.

## Initial Thoughts (Before Coding)
- Naturally when there are negative elements present, squaring them might make them bigger and the array won't be sorted
- The brute force method is to square them first, which is already O(n) and then sort it, which if optimal is still O(nlogn)
- There has to be an in place method that does it in O(n)

## Failed Attempts / Confusions
- I initially tried two pointers without considering that the largest squared values must come from the ends of the array.

## Final Approach (In Words)
- Place one pointer at the beginning and one at the end of the array.
- Compare the squares of the values at both pointers.
- The larger square must go at the end of the result array.
- Move the pointer whose value was used.
- Repeat until all elements are processed.

## Code
```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        squared_list = []
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            if (nums[l] ** 2) > (nums[r] ** 2):
                squared_list.append(nums[l] ** 2)
                l += 1
            else:
                squared_list.append(nums[r] ** 2)
                r -= 1
        
        return squared_list[::-1]
```

## Key Insights
- In a sorted array, the largest square must come from either the leftmost or rightmost element.
- Negative numbers have large absolute values on the left, while positive numbers grow on the right.
- Comparing absolute values at both ends allows us to build the result in sorted order in linear time.

