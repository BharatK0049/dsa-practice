# Problem: Valid Palindrome
LeetCode #125

## Pattern
Two pointers

## Problem Restatement
Check and see if a word when reversed is the same word as the original one. This is when all capital letters are made lowercase.
All special characters, spaces, numbers are not to be considered. Just see if the letters are repeatable reverse

## Initial Thoughts (Before Coding)
- Use functions like strip to get rid of spacing,
- Use a list to append all letters and to see when reversed if the letters match the same sequence
- Use a flag to see if I can check till when the letter is not the same

## Failed Attempts / Confusions
- Got optimal solution but used extra memory.
- Used two pointers and understood logically when to update both pointers either individually or together, but if-else block to check that was not fundamentally correct as it would allow character comparison before both pointers are guaranteed to be on valid characters.
- Tried to point a while logic stating while l != r, but that would still hold true if l = 2 and r = 1 implying that they crossed

## Final Approach (In Words)
- while l hasn't crossed r, check whether l hasn't crossed r and if l is not an alphanumeric and update l alone
- similarly check if r hasn't crossed l and update r alone
- Now check if l and r in lowercase are equal to each other or not, if not return false, else increment both by one moving closer to each other at the same time
- Make your own alnum function using ord, (easy)

## Code
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isAlNum(char):
            return ((ord(char) in range(ord('A'), ord('Z')+1)) or
               (ord(char) in range(ord('a'), ord('z')+1)) or
               (ord(char) in range(ord('0'), ord('9')+1)))
               
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not isAlNum(s[l]):
                l += 1
            
            while r > l and not isAlNum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True
```

## Key Insights
- Pointer movement and character comparison must be separated to preserve correctness.
- Inner while loops just check once and don't run n^2 times.
- the pointers move together when the letter/number is same, but if either one has a special character, they move alone
