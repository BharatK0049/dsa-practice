# Problem: Merge Sorted Array
LeetCode #88

## Pattern
Two-Pointers (Backwards-Merge)

## Problem Restatement
Given two arrays, the first one being of length 'm+n' and second being 'n', the first array contains m valid elements followed by n empty slots, and must be merged with the second array in sorted order.

## Initial Thoughts (Before Coding)
- I can just remove the last n digits from the first array, then use a temporary array to add both the arrays and then use a sort() function to get the job done
- And then I just copy it back to the original array. 

## Failed Attempts / Confusions
- Brute force - O(n^2): Remove the unnecessary elements in the first array, then adding the two arrays in a temporary array and sorting the array on top

## Final Approach (In Words)
- Use two pointers, the first one pointing from the last from the second array and the second one, pointing at 'm' of first array.
- Check if the number in the second array is larger than the first or not, if so then add it to the last of the first array and decrease the n pointer by 1
- Otherwise, add the mth element of the first array at the last and decrease m pointer by 1
- reduce last_index by 1 per iteration while m and n are both greater than 0
- If m happens to reduce to 0 first, which is when there are elements in n that are smaller than m (edge case). Then we loop again till n becomes 0 and add all the elements in the same manner at the last index.

## Code
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_index = m + n - 1

        # Starting from mth position of nums 1 and nth position of nums2 and adding from behind 
        while m > 0 and n > 0:
            if nums2[n-1] > nums1[m-1]:
                nums1[last_index] = nums2[n-1]
                n -= 1
            else:
                nums1[last_index] = nums1[m-1]
                m -= 1
            last_index -= 1
        
        # In case there is no element in nums1 that is lesser than the leftover elements in nums2
        while n > 0:
            nums1[last_index] = nums2[n-1]
            n -= 1
            last_index -= 1
        
```

## Key Insights
- Merging from the back avoids overwriting unprocessed elements in nums1.
- At each step, placing the largest remaining element guarantees correctness.
- Any remaining elements in nums2 must be copied, while remaining elements in nums1 are already in place.
