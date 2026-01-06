## Two Pointers Pattern

### When to Suspect It
- The input is **sorted** (or can be sorted)
- You are comparing **pairs** of elements
- You need to find two elements that satisfy a condition
- The problem asks to do something **in-place**
- You want to reduce a brute-force `O(n²)` search to `O(n)`

### Core Idea
Use two indices that move through the array in a coordinated way so that each element is visited at most once, exploiting order or monotonic movement.

### Key Decisions
- Do pointers move **towards each other** or in the **same direction**?
- What condition determines which pointer moves?
- Is the array sorted, or do you need to sort first?
- Are you overwriting values (in-place) or just checking conditions?

### Common Mistakes
- Applying two pointers on an **unsorted array** without justification
- Moving both pointers blindly without a monotonic rule
- Forgetting that sorting may change required indices
- Confusing two pointers with sliding window

### Canonical Problems
- Two Sum II (Input Array Is Sorted)
- Remove Duplicates from Sorted Array
- Move Zeroes
- Container With Most Water
- Valid Palindrome

### One-Sentence Mental Check
> If I can decide pointer movement based on a comparison that always reduces the search space, two pointers might apply.
