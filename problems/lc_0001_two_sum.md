# Problem: Two Sum
LeetCode #1

## Pattern
(What pattern does this belong to?)

## Problem Restatement
I am given an array of integers and a target number whose sum I should get from two numbers in the array. It is assumed that there is only one solution and the same number (if only in the same index) cannot be used twice.

## Initial Thoughts (Before Coding)
- I can look at every possible pair and see if it adds upto the target
- A nested loop to look at every other j value while i is fixed at leftmost
- How can I make this lesser than O(n^2)

## Failed Attempts / Confusions
- Nested loop takes a lot of time, leads to unnecessary checks.
- Tried to see if checking for a value whose target - value existed in the array, but that would often check the same number itself which violates the second rule.
- Tried to map indices to values to see if the number in the same index is being checked again or not, still violates rule 2

## Final Approach (In Words)
- 

## Code
```python
# write final code here

