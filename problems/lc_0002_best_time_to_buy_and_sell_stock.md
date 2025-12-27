# Problem: Best Time to Buy and Sell Stock
LeetCode # 121

## Pattern
(What pattern does this belong to?)

## Problem Restatement
I am given an array whose each element represents the value of a stock. I am supposed to find out the maximum profit from the day I buy to the day I sell in the future. return 0 if profit is not found.

## Initial Thoughts (Before Coding)
- I must move from left to right. For finding an element, there has to be at least a value to its right that must be greater than the given number. 
- If the numbers are in descending order, there exists no profit. There must be some way to keep in mind the previous things kept in mind.
- Reminds me a lot of the Coin change problem and most dynamic programming problems.
- Attempt 1 worded out: I will first use a for loop and for every element, check if there exists a bigger value for a profit to exist and then store that profit in a variable, eventually I will see if the profit gets increased at the end of the iteration or not. If so, that's my final profit.

## Failed Attempts / Confusions
- First brute force attempt: Time complexity O(n^2), checked if j - i was a bigger profit than the max profit and updated the max profit everytime it was. But time limit exceeds. Seems similar to last time as well.
- Reminds me of the two sum problem but it's difference only that the difference now matters.

## Final Approach (In Words)
- 

## Code
```python
# write final code here

