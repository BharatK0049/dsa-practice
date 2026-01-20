# Problem: Longest Substring Without Repeating Characters
LeetCode #3

## Pattern
(What pattern does this belong to?)

## Problem Restatement
Given a string, I have to find a long sequence of unique letters. Not a subsequence.

## Initial Thoughts (Before Coding)
- I tried to identify this as two pointers but no immediate logic came through nor did it feel right.
- Since characters are unique, I realized a hash set would be useful to just keep the unique letters.
- 

## Failed Attempts / Confusions
- Tried to add unique letters to the hash and then return length of the hash but that backfired if the unique letters are isolated from the actual long substring with many repeated letters in between.
- Tried to devise a brute force to look at every possible substring and use a helper function which is O(n) which when called inside an already nested loop, adds O(n^3) complexity.


## Final Approach (In Words)
- 

## Code
```python
# write final code here
```

## Key Insights
- A substring is not a subsequence, the letters must be adjacent.
- 
