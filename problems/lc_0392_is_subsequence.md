# Problem: Is Subsequence
LeetCode #392

## Pattern
Two Pointers (Order-Preserving Scan on Two Sequences)

## Problem Restatement
Given two strings `s` and `t`, determine whether `s` is a subsequence of `t`.  
A subsequence preserves relative order but characters do not need to be adjacent.

## Initial Thoughts (Before Coding)
- Using the `in` operator will not work because it only checks existence, not order.
- Using a set or list of characters ignores relative positioning, which is critical.
- Recalled the *Merge Sorted Arrays* problem where two pointers traverse two sequences while preserving order.
- Thought of using two pointers, one for each string, and advancing them monotonically. (Raw idea — worked.)

## Failed Attempts / Confusions
- Tried collecting indices or characters using lists, but this failed when characters existed but appeared in the wrong order.
- Initially assumed nested loops would imply `O(n²)` time complexity, which turned out to be incorrect due to monotonic pointer movement.

## Final Approach (In Words)
- Maintain two pointers: one iterating through the smaller string `s`, and one iterating through the larger string `t`.
- The pointer for `t` is initialized outside the loop over `s` so that it never resets, preserving order.
- For each character in `s`, scan forward in `t` until a matching character is found.
- When a match is found, advance both pointers and continue.
- If all characters in `s` are matched in order, return `True`; otherwise, return `False`.

## Code
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        t_pointer = 0
        for s_pointer in range(len(s)):
            while t_pointer < len(t):
                if t[t_pointer] == s[s_pointer]:
                    count += 1
                    t_pointer += 1
                    break
                # Update if current pointer is not equal to the s_pointer letter
                t_pointer += 1

        if count == len(s):
            return True
        else:
            return False
        
```

## Key Insights
- Nested loops do not imply O(n²) when one pointer moves monotonically and never resets.
- Subsequence problems depend on order preservation, not adjacency or frequency.
- Two-pointer techniques generalize beyond arrays and work naturally for strings and sequences.
- This problem is structurally similar to merge-style algorithms where elements are consumed once and never revisited.
