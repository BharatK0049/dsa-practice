# Problem:
LeetCode #567

## Pattern
Sliding Window + Frequency Count (Fixed Window)

## Problem Restatement
Given two strings s1 and s2, determine whether any substring of s2 with length len(s1) is a permutation of s1.

## Initial Thoughts (Before Coding)
- Okay, so clearly, it's not asking to look for the letters in the string, nor is it asking if the exact substring exists in that string.
- The brute force for this would be to use a helper function to generate all possible permutations of this substring and see if that substring exists in the string.

## Failed Attempts / Confusions
- Realized that brute force would lead to Time exceeded due to permutation function taking n!/(n-r)!, not to mention calling this helper function to check if this exists in the string, so something like n * n! complexity!!!
- Tried to use a hashset to store all the unique characters of string 1 and thought if I could just use two pointers to find the first occurrence of the first letter that is present and move further till it's not, but it's just a theoretical approach.
- Loses frequency information. Ex - "aab" and "ab" look identical in a set

## Final Approach (In Words)
- If len(s1) > len(s2), return False
- Create two frequency arrays of size 26:
  - One for s1
  - One for the current window in s2
- Initialize both arrays using the first window
- Slide the window one character at a time:
  - Add the new character
  - Remove the outgoing character
  - Compare frequency arrays
- If any match occurs, return True
- Otherwise, return False
  
## Code
```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Edge Case 1: if the substring is greater than the given string
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        if s1_count == s2_count:
            return True

        for i in range(len(s1), len(s2)):
            # Continuing updating the array past length s1 (past the window)
            s2_count[ord(s2[i]) - ord('a')] += 1
            # Removing the elements before len s1 (the window elements)
            s2_count[ord(s2[i-len(s1)]) - ord('a')] -= 1 

            if s1_count == s2_count:
                return True
        
        # If all else fails
        return False
```

## Key Insights
- Permutation matching reduces to frequency matching
- Sliding window size is fixed, not dynamic
- HashSets are insufficient when counts matter
- Comparing two 26-length arrays is constant time
- Avoid factorial thinking — look for invariants
