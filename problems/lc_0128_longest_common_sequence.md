# Problem: Longest Common Sequence
LeetCode #128

## Pattern
Hashmaps 

## Problem Restatement
Given an array, I must check to see what's the longest sequence that can be made. The sequence does not need to be contiguous in the array, but the values must be consecutive integers.

## Initial Thoughts (Before Coding)
- I first thought of sorting and thought if we take the min and see wherever it keeps incrementing by one and stop where it doesn't, but that makes it long.
- What if I loop through the array and first lock in a single element and see if incrementing from there onward have sequences that exist and then return that?
- Similar to the group anagrams, I can use a set holding all the possible sequences and return the length of the max sequence
- Any NlogN solution or N^2 is the array being sorted.
- Which numbers are allowed to START a sequence?

## Failed Attempts / Confusions
- I initially tried a two-pointer approach assuming consecutive numbers would appear near each other in the array, but this fails because the array is unsorted and valid sequences may extend both left and right of any chosen index.
- I attempted to build sequences incrementally using sets by checking for successors and predecessors, but this approach became fragile because clearing or extending a sequence prematurely can discard valid longer sequences that start from a different element.
- I struggled to define a single invariant that determines when a number should start a new sequence versus extend an existing one, which led to logic that depended too much on traversal order.

## Final Approach (In Words)
- 

## Code
```python
# write final code here
```

## Key Insights:
- Sequence membership depends on value relationships, not iteration order.
- A number can start the sequence if its predecessor does not exist.
