# Problem: Reverse String
LeetCode #344

## Pattern
Two Pointers

## Problem Restatement
Given an array of letters, reverse the order. Straight up

## Initial Thoughts (Before Coding)
- Use Reverse() function XDDD
- use slicing

## Failed Attempts / Confusions
- The problem itself was straightforward, but I noted that Python slicing ([::-1]) is not truly in-place due to extra memory allocation.
- 

## Final Approach (In Words)
- Use two pointer approach where you keep both pointers at extremem ends and swap them while updating them closer to the centre.
- Alternate Solution: Use a stack and replace the index with the popped values of the stack
- Solution 3: Recursively swap l and r and then call it inside with l and r updated

## Code
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # O(1) Space Optimal Solution using Two pointers
        l = 0
        r = len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
```

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # O(n) solution using stack which reverses as we push elements into it (LIFO)
        stack = []

        for i in s:
            stack.append(i)
        
        for i in range(len(stack)):
            s[i] = stack.pop()
```

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # O(n) space solution using recursion
        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l+1, r-1)
        
        reverse(0, len(s) - 1)
```

## Key Insights
- Two-pointer swapping is the most space-efficient way to reverse an array in-place.
- Built-in methods like list.reverse() are truly in-place and use O(1) extra space.
- Recursive solutions implicitly use O(n) space due to the call stack.
