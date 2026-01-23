# Problem: Longest Substring Without Repeating Characters
LeetCode #3

## Pattern
Sliding Window

## Problem Restatement
Given a string, find the maximum length of a contiguous substring such that no character appears more than once.

## Initial Thoughts (Before Coding)
- I tried to identify this as two pointers but no immediate logic came through nor did it feel right.
- Since characters are unique, I realized a hash set would be useful to just keep the unique letters.

## Failed Attempts / Confusions
- Tried to add unique letters to the hash and then return length of the hash but that backfired if the unique letters are isolated from the actual long substring with many repeated letters in between.
- Tried to devise a brute force to look at every possible substring and use a helper function which is O(n) which when called inside an already nested loop, adds O(n^3) complexity.


## Final Approach (In Words)
- Use a set to track characters in the current window
- Maintain two pointers l and r
- Expand r one step at a time
- If s[r] already exists:
    Shrink the window from the left until it doesn’t
- Track the maximum window size

## Code
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen_chars = set()
        maxLen = 0
        l = 0
        for r in range(len(s)):
            while s[r] in seen_chars:
                # Removing leftmost element even if not the actual duplicate, but will remove characters till the duplicate removed as l increases
                seen_chars.remove(s[l])
                l += 1
            # Adding characters to the set if it hasn't been visited before
            seen_chars.add(s[r])

            maxLen = max(maxLen, r - l + 1) # Current max length or current window size
            
        return maxLen
```

## Key Insights
- A substring is not a subsequence, the letters must be adjacent.
- Another amortized nested loop which doesn't make complexity N^2 due to the while loop not running n times within more than once.
- Nested loop ≠ quadratic when pointers only move forward
- Substring ≠ subsequence 
