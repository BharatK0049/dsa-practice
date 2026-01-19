# Problem: Container with most water
LeetCode #11

## Pattern
Two Pointers (greedy)

## Problem Restatement
Given an array of heights of water of various lengths, find the maximum area that can be formed between two of the lengths.  

## Initial Thoughts (Before Coding)
- A brute force approach would be to take every pair and get area as min(l1, l2) * distance between them and return the max area you get from taht.
- Since this is an array, I think of two pointers yet again. The way we would phrase the loop condition would be while max area keeps increasing, check and if it stops increasing, we assume that's the maximum possible area.
- 

## Failed Attempts / Confusions
- Figured out the brute force.
- Tried out a two pointer approach with a logicless left and right pointer updation, but understood the premise that the loop is useless once the max_area does not increase, but can't seem to figure out how to code this.

## Final Approach (In Words)
- Initialize two pointers at the extreme ends\
- Compute area using the shorter height
- Update max_area
- Move the pointer at the shorter height
- Repeat until pointers meet

## Code
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:

            if (min(height[l], height[r]) * (r-l)) > max_area:
                max_area = min(height[l], height[r]) * (r-l)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
```

## Key Insights
- Minimum height between the two heights, and the maximum distance gives you the area.
- We initialize the pointers at the extreme ends to maximize the area.
- Area is constrained by the shorter line
- Width always decreases as pointers move inward
- Moving the taller line cannot improve area
- Greedy pointer movement guarantees optimality

