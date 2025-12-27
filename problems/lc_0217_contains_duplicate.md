# Problem: Contains Duplicate
LeetCode # 217

## Pattern
(What pattern does this belong to?)

## Problem Restatement
Given an array, check and see if there exists duplicate occurrences of a number. Return True if there exist duplicates and false if all numbers are unique.

## Initial Thoughts (Before Coding)
- Sounds quite straightforward, just check if count(i) > 1 for every i. And if that works then go for true else false.
- Yep it was brute force. Turns out, using count() inside a loop counts as a nested loop. Of course it was. How am I making this O(n)??
- How about a hash map to see if the number has been checked or not?

## Failed Attempts / Confusions
- Figured out brute force (yay...) Count inside a loop leads to erm time consumption.
- Property: how to keep count of a single number without having to continuously check for its occurrences every time?

## Final Approach (In Words)
- 

## Code
```python
# write final code here
