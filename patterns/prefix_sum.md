# Prefix Sum

## When to Suspect It
- Multiple queries on sums or ranges
- You need to compute sums efficiently
- You see repeated sum computations over subarrays or range queries

## Core Idea
Precompute cumulative sums so you can get any range sum in constant time by subtraction.

## Key Decisions
- Decide whether to build prefix sums in place or in a separate array
- Determine if you need sum over contiguous ranges or arbitrary subarrays
- Use prefix sum to answer queries or optimize sliding / window logic

## Common Mistakes
- Forgetting to handle the base case (prefix array starting at 0)
- Not subtracting correctly (off-by-one errors)
- Recomputing prefix array unnecessarily

## Canonical Problems
- Range Sum Query – Immutable (LeetCode #303)
- Contiguous Array (LeetCode #525)
- Subarray Sum Equals K (LeetCode #560)
