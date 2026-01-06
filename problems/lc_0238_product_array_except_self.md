# Problem: Product of Array Except Self
LeetCode #238

## Pattern
Prefix and Suffix Accumulation (Prefix Sum type)

## Problem Restatement
Given an array with integers, I must return an array of the same size where each corresponding index has the product of the numbers in the input array except that number.
I am not allowed to use division so that rules out my initial thoughts. Must learn to read the entire problem statement than jumping into approaches.

## Initial Thoughts (Before Coding)
- For each 'i', I can just multiply all elements and divide by that particular element itself to remove that multiplication.
- I can multiply all elements in a separate for loop or use some product function that exists. 
- Then just return that array, looks simple right?
- Think I need to use recursion here but don't know how..
- Does using numpy array multiplication count or is that cheating?

## Failed Attempts / Confusions
- Tried to multiply every other number after ith index in jth inner loop but that overlooks the numbers to the left of i.
- Used two lists, one to remove the number itself and multiply every other element and another to store the final product, all this was done in O(N^2)
- Property: Can I reduce having to perform multiplication of every other number when it's evident that I have to just multiply it all once and then remove that number?
- Can't be using division since 0s exist and that would lead to zero division error.
- I managed to solve it using division operator, a stupidly lengthy code and it worked.. but it was cheating. I even bypassed using power (-1) but that's division too. At least I know how to solve it this way. Now to actually solve the problem
- answer[i] = (product of nums[0 … i-1]) × (product of nums[i+1 … n-1])
- I initially relied on nested loops to compute prefix and postfix products separately before realizing they can be accumulated in linear time.

## Final Approach (In Words)
- Using one output array as space, I first use a for loop to update all the prefix products of the number by taking a prefix variable and storing the output_array's index value as that, followed by prefix multiplication.
- I repeat this using another loop and a postfix variable and again allocate the postfix value to the output_array's index, however I don't just directly allocate it but multiply it to preserve the prefix value, this time followed by postfix multiplication. The loop starts from n-1 and goes to 0.

## Code
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output_arr = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            output_arr[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output_arr[i] *= postfix
            postfix *= nums[i]

        return output_arr
```

## Key Insight
For each index, the required product is the product of all elements to its left multiplied by the product of all elements to its right, which can be precomputed using prefix and suffix products.
