# Problem: Best Time to Buy and Sell Stock
LeetCode # 121

## Pattern
Two-Pointer

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
- Tried to formulate an equation similar to two sum this time price[j] - price[i] = profit and rewriting it should give profit + price[i] = price[j], but that didn't seem to work as I can't work with the right indices and I'm not supposed to get the indices to begin with. I tried to have key value pairs of the value itself so it'd return the value but it shows as 0. It doesn't work because profit starts as 0 and can only be updated when we get hold of j and i first.
- Saw something where it is done in-place.
- Property: For any selling day, only the minimum buying price so far matters.
- Note: Pair-based problems often collapse into single-pass solutions, but what they collapse into depends on whether the question asks for existence or optimality.

## Final Approach (In Words)
- According to the Neetcode solution, I will take two pointers, one to track the buying price and the other, the selling. We use a single while loop to see if the right price is greater than the left one, and if so we calculate profit. Then we check and see if it's the max profit or not and we progress by moving the left to the right pointer and incrementing the right pointer by one.
- Simply put, if my selling price is greater than my buying price, I calculate profit and check to see if it's the maximum profit or not. Otherwise, I move the buying to the current selling and increment the selling to the next price.

## Code
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            # Checking if sale is profitable
            if prices[sell] > prices[buy]:
                # Checking if current profit is the max profit
                if prices[sell] - prices[buy] > profit:
                    profit = prices[sell] - prices[buy]
            # Moving the buy pointer to the current selling as it's lesser and moving the selling point to the next price    
            else:
                buy = sell
            sell += 1
        
        return profit

