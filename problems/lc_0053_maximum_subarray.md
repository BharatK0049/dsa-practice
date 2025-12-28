# Problem: Maximum Subarray
LeetCode #53

## Pattern
Greedy Single-Pass State Tracking (Kadane’s Algorithm)

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
- Thought of moving left pointer whenever the sum from left upto one before right is lesser than 0 as it does not contribute to the sum but it doesn't work when there are two negative numbers.

## Final Approach (In Words)
- Looking through the neetcode solution, I understood that a problem that looks like a sliding window problem isn't when it isn't being slid under a fixed condition.
- I take the max sum to be the first element (normal approach to assume, or just take -infinity) and track the current sum of numbers from left to right starting from 0
- One major thing to note is when prefix sum of numbers is negative, it is not likely to contribute to the subarray with the max sum, so we reset that sum to 0 and keep adding the elements one by one. that way we are adding each step and not taking sum of all each iteration, reducing complexity from n^2 to n.
## Code
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSum = max(maxSum, curSum)
        
        return maxSum
```
## Key Insights
- This here is not a sliding window problem even if it looks like it. Why because, Sliding window is about managing a range under a condition
- A negative subarray sum cannot help form a maximum subarray in the future, so it is optimal to discard it and start fresh from the next element.
- Sliding window requires a rule for shrinking or expanding the window when the condition breaks, which isn't true for cases like [-2, -1]
