# Problem: Find the Index of the First Occurence in a String
LeetCode #28

## Pattern
-

## Problem Restatement
Given a string (haystack) and a needle (smaller string), find the first occurence in the string. Like the substring if I must put it that way.

## Initial Thoughts (Before Coding)
- Two pointers, just take the left pointer from the beginning and the right pointer one after the left.
- Once the left has been found, start right one after left and loop till right pointer is the last elemtn of the needle. 
- Assuming that all letters in between are of the needle letters

## Failed Attempts / Confusions
- One edge case is when there is only one letter needle, so r = l+1 becomes useless. Plus using a while True loop makes the logic very flawed.
- Also right = left + 1 is flawed when there are double letters so it automatically leaves the loop and returns wrong index.
- Recognized this to be a sliding window variation of two pointers and assigned right pointer as len(needle) - 1. Moved l and r by 1 when either of the case wasn't satisfied

## Final Approach (In Words)
- 

## Code
```python
# write final code here
```

## Key Insights
- In a sliding window problem, both pointers move at the same time. (this is not exactly a sliding window problem, at least not with two pointers)
- 
