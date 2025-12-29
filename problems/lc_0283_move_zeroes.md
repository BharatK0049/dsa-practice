# Problem: Move Zeroes
LeetCode #283

## Pattern
Two Pointers (In-Place Reordering)

## Problem Restatement
Given an array, without using an additional array, move all the existing zeroes to the right of the array while keeping the non zero elements to the left.

## Initial Thoughts (Before Coding)
- Can use a nested loop to see if the ith element is 0 and jth element is not, and then swap bubble sort style.
- I've solved this problem before back in June 2025 using an optimal solution and I'm not even aware of it.
- I messed up seeing the optimal solution before even thinking it through

## Failed Attempts / Confusions
- The brute force.
- Saw the solution without putting my own effort. But I forgot the solution immediately so the problem still counts.
- Still feel must do this again at the checkpoint day
- Property: At any point, all elements before index l are guaranteed to be non-zero.

## Final Approach (In Words)
- I maintain a pointer `l` that tracks the position where the next non-zero element should be placed.
- As I iterate through the array, whenever I encounter a non-zero value, I swap it with the element at `l` and increment `l`.
- This guarantees that all non-zero elements remain in order on the left, and all zeroes move to the right.


## Code
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
```

## Key Insight:
The problem is not about sliding a window but about partitioning the array in place. 
By tracking the next position for a non-zero element, we can move all zeroes to the end while preserving order.
