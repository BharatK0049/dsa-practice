# Problem: Reverse Words in a String
LeetCode #151

## Pattern
Two-Pointers

## Problem Restatement
Given a sentence, reverse the sequence of words in the sentence and remove all trailing whitespaces and unnecessary spaces in between.

## Initial Thoughts (Before Coding)
- I can use strip function to get rid of trailing spaces
- Use split function to get all the words in a list
- Then iterate backwards and add it to a new string and then return the string but not the last space, which is jugaad.

## Failed Attempts / Confusions
- Split and stripped the string, then added every word to a new string but that took O(N^2) due to strings being immutable.

## Final Approach (In Words)
- Strip all whitespaces using strip() function
- Split the string into words in a string whenever there is a ' '
- In that list, just reverse that list using two pointers (same approach as reversing a string)
- use join function to join the list elements with a " " and return that string

## Code
```python
class Solution:
    def reverseWords(self, s: str) -> str:

        s.strip()

        words = s.split()

        l = 0
        r = len(words) - 1

        while l < r:
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1
        
        return " ".join(words)
```

## Key Insights
- Adding a new character to a string iteratively does not take O(n) but O(n^2) due to a new space being allocated to the string (strings are immutable)
- Having all the words, stripped of whitespaces in a list and then reversing the order of the list is genius. 
