# Problem: Rotate Array
LeetCode #189

## Pattern
(What pattern does this belong to?)

## Problem Restatement
Given an array, I have to rotate it k number of times in place without returning an array.

## Initial Thoughts (Before Coding)
- Can use an additional list to slice the original list at the kth index from last and shift it to the beginning and the rest go to the last.
- Double extend function

## Failed Attempts / Confusions
- My first instinct was to create a temporary list, append the last k elements of the array to it, then append the remaining elements from the front, and finally copy everything back into the original array to satisfy the “in-place” requirement.
- This approach works when k is smaller than the length of the array, but it fails when k is greater than the number of elements. In those cases, slicing from len(nums) - k does not behave the way I intuitively expect.
- I realized that Python slicing does not throw an out-of-bounds error. Instead, it silently adjusts the slice, which leads to unexpected results when k is larger than the array size.
- I attempted to handle the case where k > len(nums) by reducing k using modulo (k % len(nums)), reasoning that rotating by the array length should result in the same array.
- After introducing the modulo logic, I tried to handle even-length and odd-length arrays separately, assuming the split point would differ based on parity. This led to overly complex conditional logic.
- This version still caused index-out-of-range errors when copying values back into nums, indicating that the constructed rotated_list did not always have the correct size or ordering.
- I eventually arrived at a correct solution using an auxiliary array by first normalizing k with modulo and then reconstructing the rotated order as last k + first n-k. While this solves correctness issues and edge cases, it does not satisfy the in-place constraint.

## Final Approach (In Words)
- 

## Code
```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        # Reversing the whole array Eg: [7, 6, 5, 4, 3, 2, 1]
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        # Reversing the first half upto k Eg: [5, 6, 7, 4, 3, 2, 1]
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        # Reversing the second half from k to end Eg: [5, 6, 7, 1, 2, 3, 4]
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
```
