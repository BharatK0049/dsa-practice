# Problem: Contains Duplicate
LeetCode #217

## Pattern
Existence Check via Hashing

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
- I use a set, which is similar to a hashmap the way I intend to use it. I keep track of unique numbers in it as a set cannot have duplicate and add numbers that I encounter for the first time.
- I set the flag to true if I encounter a number that I've seen before. Otherwise the flag stays false.

## Code
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        flag = False
        seen = set()
        for i in nums:
            # If element has already been seen
            if i in seen:
                flag = True
            else:
                seen.add(i)
```

## Key Insight
Instead of repeatedly scanning the array to count occurrences, I only need to know whether I’ve seen a value before, which can be tracked in constant time using a set.
        return flag
