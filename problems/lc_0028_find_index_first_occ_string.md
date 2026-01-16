# Problem: Find the Index of the First Occurence in a String
LeetCode #28

## Pattern
Substring Search (Naive)

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
- Using a brute force O(m * n) approach to loop through the haystack's length - the needle's length + 1 to save needle length's spaces left that can be checked by the inner loop to avoid any out of index errors.
- Within the inner loop, check to see if the haystack's index of i+j matches the needle's j index and break if there's if it doesn't match. Move to next i.
- If inner loop has been completed successfully with no breaks, return the corresponding ith index as index of first occurrrence.
- Return -1 for no matches.

## Code
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Looping through 0 to the last index where there is len(needle) - 1 characters left 
        for i in range(len(haystack) - len(needle) + 1):
            # Inner window to see if the substring letters all match from the starting point of i
            for j in range(len(needle)):
                # If where we start from i to j letters forth (substring length) doesn't match the letters in needle, then we move to the next ith index
                if haystack[i+j] != needle[j]:
                    break
                # If inner loop has run successfully i.e. all letter have matched in that window
                if j == len(needle) - 1:
                    return i
            # When substring does not match
        return -1
```

## Key Insights
- This problem checks every possible fixed-length window of size `m` in the haystack.
- No partial match allows safe skipping of future windows, so every alignment must be verified.
- The inner loop validates a single alignment character-by-character and exits early on mismatch.
- The outer loop only runs until `n - m + 1` to avoid out-of-bounds access.

