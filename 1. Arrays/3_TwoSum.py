# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Brute Force Method
# Time Complexity: O(n^2)
# Space Complexity: O(n)


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    indices = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                indices.append(i)
                indices.append(j)
    
    return indices

# Test Case:
print(twoSum([2,7,11,15], 22))

# Neetcode Solution: Hashmaps
# Time Complexity: O(n)
# Space Complexity: O(n)

def twoSumHash(nums, target):
    indices = {}
    listindices = []
    for i in range(len(nums)):
        if (target - nums[i]) not in indices:
            indices[nums[i]] = i
        else:
            listindices.append(indices[target-nums[i]])
            listindices.append(i)
    
    return listindices

# Test Case:
print(twoSumHash([2,7,11,15], 9))
