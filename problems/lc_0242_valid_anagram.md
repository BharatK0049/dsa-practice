# Problem: Valid Anagram
LeetCode #242

## Pattern
Hashmap

## Problem Restatement
Given two strings, see if they're anagrams. Check if each letter in both words have the same number of occurrences.

## Initial Thoughts (Before Coding)
- We're looking at letter frequencies, boom hashmap.
- Probably take two hashmaps, one for the first string, the second for the other and then see which values match if the keys match to begin with.

## Failed Attempts / Confusions
- Used count function inside loop to check if the number of letter occurrences in t was the same as s. O(n^2)

## Final Approach (In Words)
- Check if both strings are of equal length or not, return false if so.
- Use one hashmap and first get all frequencies of all letter in first string.
- Move to the second string and see if the letter exists in hashmap already, if not then straight up return false, else reduce by 1
- If both strings contain the same letters with the same frequencies, incrementing counts for one string and decrementing for the other will result in all frequencies becoming 0.

## Code
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        hashmap = {}

        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        for i in t:
            if i not in hashmap:
                return False
            else:
                hashmap[i] -= 1
        
        for i in hashmap:
            if hashmap[i] != 0:
                return False
        return True
```
## Key Insight
- Instead of maintaining two separate frequency maps, we can track the net frequency difference using a single hashmap.
- By incrementing counts for one string and decrementing for the other, all values must cancel out to zero for the strings to be anagrams.
