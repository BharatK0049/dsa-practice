# Problem: Roman to Integer
LeetCode #13

## Pattern
Hashmap

## Problem Restatement
Given a string in roman numeral, convert it to its integer equivalent. Constraint is that roman numerals are in the range 1, 3999

## Initial Thoughts (Before Coding)
- Use a hashmap to map each Roman numeral to its integer value.
- Handle subtractive pairs (IV, IX, XL, XC, CD, CM) explicitly using condition checks.
- decrement by 2 everytime we encounter a prefix case, so we don't count that indivually and by 1 when it's just an individual numeral with no prefix.
- When a subtractive pair is detected, add its value and decrement the index by 2; otherwise, add the value of the single numeral and decrement by 1.

## Failed Attempts / Confusions
- Initially accessed s[i-1] without guarding for i == 0, which caused negative indexing and incorrect behavior due to Python wrapping negative indices.
- Tried to handle the first character separately, but this says nothing about whether it participates in a subtractive pair.
- Overfocused on special cases instead of explicitly defining when subtractive logic is allowed.

## Final Approach (In Words)
- Use a hashmap to store integer values of Roman numerals.
- Traverse the string from right to left using an index i.
- At each step, check for subtractive pairs only if i > 0, since subtractive notation requires two characters.
- If a valid subtractive pair is found, add its corresponding value and move the index back by 2.
- Otherwise, add the value of the current numeral and move the index back by 1.
- Continue until all characters are processed and return the accumulated sum.

## Code
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        
        filthy_romans = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        # Base case:
        if s in filthy_romans:
            return filthy_romans[s]
        
        if s == '':
            return 0
        
        number = 0
        i = len(s) - 1
        while i >= 0:
            if i > 0:
                if s[i-1] == 'I' and s[i] == 'V':
                    number += 4
                    i -= 2
                    continue

                if s[i-1] == 'I' and s[i] == 'X':
                    number += 9
                    i -= 2
                    continue
                
                if s[i-1] == 'X' and s[i] == 'L':
                    number += 40
                    i -= 2
                    continue
                
                if s[i-1] == 'X' and s[i] == 'C':
                    number += 90
                    i -= 2
                    continue
                
                if s[i-1] == 'C' and s[i] == 'D':
                    number += 400
                    i -= 2
                    continue
                
                if s[i-1] == 'C' and s[i] == 'M':
                    number += 900
                    i -= 2
                    continue

            if s[i] in filthy_romans:
                number += filthy_romans[s[i]]
                i-= 1
    
        return number
```

## Key Insights
- Subtractive Roman numeral logic is only valid when a previous character exists, so accessing i-1 demonstrates the need for an explicit boundary invariant (i > 0).
- Python’s negative indexing can silently introduce logical bugs if invariants are not enforced.
- Iterating from right to left simplifies subtractive handling by letting larger values naturally dominate unless overridden by a valid subtractive pair.
