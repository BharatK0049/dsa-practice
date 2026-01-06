# Problem: Group Anagrams
LeetCode #49

## Pattern
Hashmap with frequency signature

## Problem Restatement
I have a list of words, I must return a nested list, where each inner list must be the anagram words grouped..

## Initial Thoughts (Before Coding)
- God dayum. How on Earth am I achieving this
- Already thinking of checking for edge cases like the list being empty or it just having a single word; feels like jugaad to me.
- From problem 242 - Valid Anagrams, I'll just take that function instead of coding it all over again, it's not cheating if I did it before (for now) for the raw solution.

## Failed Attempts / Confusions
- I incorrectly used a set to track seen values, which caused duplicate words at different indices to be skipped even though grouping requires preserving all occurrences.
- My brute-force nested-loop approach worked logically but became inefficient and fragile due to mixing anagram checking with value-based deduplication.
- I learned that grouping problems must track elements or indices, not just unique values, because duplicates are meaningful group members.

## Final Approach (In Words)
- create a 26 size array with numbers that store frequency of characters seen in each word
- Loop through each word within the list and get the frequency of each character and update the list
- create a key value pair where the key is a tuple version of lowercase list frequency (coz immutable) and each word that matches this frequency map
- lastly, create a list of the values of the dictionary and return that list.
- Use defaultdict(list) so that even if key doesn't exist, automatically create it with an empty list value.

## Code
```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        pat_hash = defaultdict(list)
        for i in strs:
            lwr_case = [0] * 26
            # Loop through the letter 'i'
            for j in i:
                lwr_case[ord(j) - ord('a')] += 1
            
            pat_hash[tuple(lwr_case)].append(i)
        final_list = []
        for i in pat_hash:
            final_list.append(pat_hash[i])
        
        return final_list
```
## Key Insight
Anagrams can be grouped by mapping each word to a canonical frequency signature; words with identical character frequency distributions belong to the same group regardless of order.
