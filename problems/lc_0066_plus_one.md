# Problem:
LeetCode #66

## Pattern
Simulation (Carry Handling)

## Problem Restatement
I have an array which represents digits of a number. I am to return an array with digits but the number should be incremented by one. 
Like the units digit must be increased by one.

## Initial Thoughts (Before Coding)
- Can it be done in O(1)? Just see if the last digit is <9, then just add one to the last element and return list. 
- If element is 9, then one of two things can happen, either there is a pre-existing number out there and I can just add 1 to the number before it and make the 9 a 0, or I add a 1 to the left of the nine and make the 9 a 0
- Property: Adding 1 to a number means:
-   start from the rightmost digit
-   propagate carry left as long as digits are 9
-   stop as soon as a digit is less than 9

## Failed Attempts / Confusions
- I initially handled only the last digit and the digit before it, which fails when there are multiple trailing 9s.
- The correct approach requires propagating the carry left until it can be absorbed.


## Final Approach (In Words)
- Start from the last digit and move left.
- If the current digit is less than 9:
-   increment it by 1
-   return the array immediately.
- If the current digit is 9:
-   set it to 0
-   continue moving left with carry.
- If all digits were 9:
-   insert 1 at the front of the array.

## Code
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nine_count = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                nine_count += 1
                digits[i] = 0

        if nine_count == len(digits):
            digits.insert(0, 1)
        return digits
```

## Key Insight
Incrementing a number represented as digits requires propagating a carry from right to left until a digit less than 9 is found; if all digits are 9, a new leading 1 must be added.
