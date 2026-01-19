# Problem: Two Sum II
LeetCode #167

## Pattern
(What pattern does this belong to?)

## Problem Restatement
Similar to two sum, there are two integers that add up to the final target solution, only that the given array is in non decreasing order, elements sorted.

## Initial Thoughts (Before Coding)
- Brute force remains `O(n²)` and is not acceptable.
- A hashmap solution works in `O(n)` time but uses `O(n)` extra space.
- Since the array is sorted, there must be a way to exploit ordering and avoid extra space.
- Recalled the two-pointer technique used in merge-style problems.

## Failed Attempts / Confusions
- Reused the Two Sum I hashmap approach, which worked but ignored the sorted constraint.
- Implemented a two-pointer approach but forgot to explicitly handle the equality case.
- Assumed Python would “implicitly” return when neither `<` nor `>` condition was met.
- Learned that control flow must explicitly encode the termination condition.

## Final Approach (In Words)
- Place one pointer at the start (`l`) and one at the end (`r`) of the array.
- While `l < r`:
  - If the sum is greater than the target, decrement `r` to reduce the sum.
  - If the sum is less than the target, increment `l` to increase the sum.
  - Otherwise, the sum equals the target — return the 1-based indices immediately.
- This works because the sorted order guarantees that pointer movements monotonically eliminate impossible pairs.

## Code
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]
```

## Key Insights
- Sorted input is a strong signal that a two-pointer elimination strategy exists.
- The equality case (sum == target) must be handled explicitly; Python does not infer it.
- Two Sum II improves upon Two Sum I by reducing space complexity from O(n) to O(1).
- When exactly one solution is guaranteed, encountering it should immediately terminate the algorithm.
