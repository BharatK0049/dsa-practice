# Problem: Longest Common Prefix
LeetCode #14

## Pattern
Horizontal Scanning (Character-by-Character Verification)

## Problem Restatement
Given a list of words, return the largest prefix out of the words, otherwise an empty string if no such prefix exists.

## Initial Thoughts (Before Coding)
- Take the smallest word and loop through those letters to see which all are in the words
- Thought of using the in operator
- If all words agree at a given character position, that character is part of the prefix.

## Failed Attempts / Confusions
- Initially assumed the shortest word’s characters would naturally form the prefix if they appeared in all other words, but this failed when characters existed at different starting positions.
- Got the solution using indices but feel like I didn't actually use a logical solution and the whole thing feels ad-hoc (brute force O(m * n))
- Attempted to use the first word as the reference without bounding by the shortest length, which caused index errors when other strings were shorter.
## Final Approach (In Words)
- Identify the shortest string to establish the maximum possible prefix length. (Key insight, the largest possible prefix can be the shortest string in the list of words)
- Iterate character by character (column-wise) across all strings.
- At each index, compare the current character of the shortest word with the corresponding character in every other word.
- If any mismatch occurs, immediately return the prefix built so far.
- If all strings match at that index, extend the prefix.
- If all characters of the shortest word are validated, return it as the longest common prefix.
## Code
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        short_wrd = strs[0]

        for i in strs:
            if len(i) < len(short_wrd):
                short_wrd = i
                
        prefix_wrd = ""
        for i in range(len(short_wrd)):
            for j in range(len(strs)):
                if short_wrd[i] != strs[j][i]: # Comparing the characters rather than slices
                    return prefix_wrd
                
                if j == len(strs) - 1:
                    prefix_wrd = short_wrd[:i+1]
        
        return prefix_wrd
```

## Key Insights
- In longest common prefix problems, you don’t need to build the prefix incrementally — you only need to detect the first index where characters stop matching.
- The shortest string provides a strict upper bound on prefix length and prevents index errors.
- Unrelated to problem, but I realize that when solving leetcode problems, look for a solution that is supposed to solve all test cases and maybe tweak a few pitfalls rather than looking for potential pitfalls and tweaking those first.
- When comparing characters column-wise across strings, the loop bound must be the length of the shortest string, otherwise index errors are inevitable.
