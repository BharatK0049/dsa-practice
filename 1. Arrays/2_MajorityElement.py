# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def majorityElementBrute(nums):
    max_count = 0
    maj_ele = 0
    for i in range(len(nums)):
        if nums.count(nums[i]) > max_count:
            max_count = nums.count(nums[i])
            maj_ele = nums[i]
    
    return maj_ele

# Test case
print(majorityElementBrute([2,2,1,1,1,2,2]))

# My Solution: Dictionary Approach (Hashmap)
# Time Complexity: O(n)
# Space Complexity: O(n)

def majorityElementHash(nums):
    
    ele_counts = {}
    max_val = 0
    for i in nums:
        if i not in ele_counts:
            ele_counts[i] = 1
        else:
            ele_counts[i] += 1
    
    for i in ele_counts:
        if ele_counts[i] == max(ele_counts.values()):
            max_val = i

    return max_val

# Test Case
print(majorityElementHash([2,2,1,1,1,2,2]))

# Neetcode Solution: Boyer-Moore Solution (Optimized Space complexity) {Limitation: Input has to have majority element. There cannot be a tie}
# Time Complexity: O(n)
# Space Complexity: O(1)

def majorityElementOptimized(nums):
    j = 0
    maj = 0
    count = 0
    for i in range(len(nums)):
        
        if count == 0:
            j = i
            maj = nums[j]

        if nums[i] == nums[j]:
            count += 1
        else:
            count -= 1

    return maj

# Test Case
print(majorityElementOptimized([2,2,1,1,1,2,2]))
