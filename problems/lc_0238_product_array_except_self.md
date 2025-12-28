# Problem: Product of Array Except Self
LeetCode #238

## Pattern
(What pattern does this belong to?)

## Problem Restatement
Given an array with integers, I must return an array of the same size where each corresponding index has the product of the numbers in the input array except that number.
I am not allowed to use division so that rules out my initial thoughts. Must learn to read the entire problem statement than jumping into approaches.

## Initial Thoughts (Before Coding)
- For each 'i', I can just multiply all elements and divide by that particular element itself to remove that multiplication.
- I can multiply all elements in a separate for loop or use some product function that exists. 
- Then just return that array, looks simple right?
- Think I need to use recursion here but don't know how..
- Does using numpy array multiplication count or is that cheating?

## Failed Attempts / Confusions
- Tried to multiply every other number after ith index in jth inner loop but that overlooks the numbers to the left of i.
- Used two lists, one to remove the number itself and multiply every other element and another to store the final product, all this was done in O(N^2)
- Property: Can I reduce having to perform multiplication of every other number when it's evident that I have to just multiply it all once and then remove that number?
- Can't be using division since 0s exist and that would lead to zero division error.

## Final Approach (In Words)
- 

## Code
```python
# write final code here
