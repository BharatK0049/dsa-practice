# Problem: Group Anagrams
LeetCode #49

## Pattern
(What pattern does this belong to?)

## Problem Restatement
I have a list of words, I must return a nested list, where each inner list must be the anagram words grouped..

## Initial Thoughts (Before Coding)
- God dayum. How on Earth am I achieving this
- Already thinking of checking for edge cases like the list being empty or it just having a single word; feels like jugaad to me.
- From problem 242 - Valid Anagrams, I'll just take that function instead of coding it all over again, it's not cheating if I did it before (for now) for the raw solution.
- 

## Failed Attempts / Confusions
- I incorrectly used a set to track seen values, which caused duplicate words at different indices to be skipped even though grouping requires preserving all occurrences.
- My brute-force nested-loop approach worked logically but became inefficient and fragile due to mixing anagram checking with value-based deduplication.
- I learned that grouping problems must track elements or indices, not just unique values, because duplicates are meaningful group members.

## Final Approach (In Words)
- 

## Code
```python
# write final code here
