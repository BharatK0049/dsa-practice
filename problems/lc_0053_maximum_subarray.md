# Problem: Maximum Subarray
LeetCode #53

## Pattern
Two-pointer (sliding window)

## Problem Restatement
I am given an array, and I should find the largest subarray whose sum gives me the highest possible value.

## Initial Thoughts (Before Coding)
- Clearly, this means the array itself could be the largest if the sum of the elements is big.
- The brute force for this could be to just get all possible subarrays using slicing and seeing which one is the max.
- Property: Need to find a way to avoid looking at every possible subarray which takes n^2 time
- What if I started with the whole array and removed the smallest number and checked to see if the max number changed or not?
- I feel this is some kind of sliding window problem, but I cannot think of how to find that approach, two pointers isn't the way..

## Failed Attempts / Confusions
- I got the brute force working with a time complexity of O(N^2) where I check every possible slice (subarray) and compare to see if the sum obtained from the elements is max or not. Takes too much time. started with max sum being the first element value
- I tried to start with the largest array and remove the smaller ones but that led to a major flaw. The subarray is not conssiting of elements that are adjacent but can be far away too. It's not in place and only takes the largest elements.. could be a solution for a different kind of max subarray. Think I can stick to max sum being the sum of the entire array as that's possible for the entire array to be the largest subarray. We divide into smaller if possible.
- Thought of using two pointers but it doesn't solve it any different than one pass since both pointers must be updated n times each making it n^2 still.
- I will start both left and right pointer on the first element and keep the maxsum as first element too. whenever left is a negative number and right is a number greater, I move the left pointer to the rightmost?

## Final Approach (In Words)
- Okay, went through the neetcode explanation without looking at the solution code, I have a rough idea in mind, similar to the buying and selling stocks.
- 
## Code
```python
# write final code here

