# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def moveZeroes(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

# Test Cases
print(moveZeroes([0, 4, 4, 65, 7, 43, 0, 6, 0, 3, 2, 0, 7, 0, 6, 0, 2]))

# NeetCode Solution: Two pointer Technique
# Time Complexity: O(n)
# Space Complexity: O(1)

def moveZeroes(nums):
    left_ptr = 0
    for right_ptr in range(len(nums)):
        if nums[right_ptr]:
            nums[left_ptr], nums[right_ptr] = nums[right_ptr], nums[left_ptr]
            left_ptr += 1
    return nums

print(moveZeroes([0, 4, 4, 65, 7, 43, 0, 6, 0, 3, 2, 0, 7, 0, 6, 0, 2]))