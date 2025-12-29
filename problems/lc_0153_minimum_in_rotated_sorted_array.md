# Problem: Find Minimum in Rotated Sorted Array
LeetCode #153

## Pattern
Binary Search

## Problem Restatement
I am given a *sorted* array which has been rotated some number of times. Now in this sorted but rotated array, I need to find the smallest element in a time of log(n)

## Initial Thoughts (Before Coding)
- Before even reading log(n), I just did a litmus test to see if the submission would accept an N time solution (i.e. using min(x) or just assigning minEle to the smallest element in the list using a for loop that runs n times.
- Afterward, seeing the log n reminded me of binary search, so went to revise that.
- 

## Failed Attempts / Confusions
- Implemented binary search, took the least element to the first element, and then went with the standard blueprint of binary search. If it was greater than min, we would increase left, if it was lesser, we would decrease and make the min element equal to the middle. And if it happened to be middle, we returned that. THe flaw is with just two elements in the list, ex: [2,1], my logic kinda flawed since left and right is just 0 and 1 and the middle is just 2.. and i just return that. 
- Later tried to make min_el as infinity and that made it even worse just returning my first element.

## Final Approach (In Words)
- Did some jugaad and checked for cases where there were only two elements and the rightmost was the least and returned that. It accepted all 150 cases so we take that as a win
- But that isn't how things are to be approached so I'll get the "legit" solution.
- THe real solution: Start like how you normally would with binary search, have a left and right pointer, and while l <= r, calculate the middle. Here we check to see if the middle index's value is greater than right or not. If so, we move the left by one, i.e moving to the rightmost half which is sorted. Otherwise, we half the right to middle, staying in the leftmost. We return the leftmost index, i.e. when the left equals right.

## Code
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # Strictly checking left index lesser than right. We find min when left = right
        while l < r:
            m = (l + r) // 2
            # Seeing which side is sorted, right or left
            if nums[m] > nums[r]:
                # Moving to the right half
                l = m + 1
            else:
                # Staying in the left half
                r = m
        
        return nums[l]
```

## Key Insight
- In a rotated sorted array, one half is always sorted; by comparing the middle element with the rightmost element, we can determine which half contains the rotation point and discard the other half using binary search until only the minimum remains.
