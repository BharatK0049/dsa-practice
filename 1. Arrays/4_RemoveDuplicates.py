# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Brute Force Method (it works but not according to da judge)
# Time Complexity: O(n)
# Space Complexity: O(n)

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    unique_elements = []
    for i in nums:
        if i not in unique_elements:
            unique_elements.append(i)
        else:
            continue
    nums = unique_elements
    print(nums)
    return len(nums)

# TestCase:
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

# Intended Solution
# Time Complexity: O(n)
# Space Complexity: O(1)

def removeDuplicatesInPlace(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left_ptr = 1
    for right_ptr in range(1, len(nums)):
        if nums[right_ptr-1] == nums[right_ptr]:
            continue
        else:
            nums[left_ptr] = nums[right_ptr]
            left_ptr += 1
    print(nums)
    return left_ptr

# TestCase:
print(removeDuplicatesInPlace([0,0,1,1,1,2,2,3,3,4]))