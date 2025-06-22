# Given an integer x, return true if x is a palindrome, and false otherwise. 

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# My solution:
# Time Complexity: O(log(n))
# Space Complexity: O(1)

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    temp = x
    rem = 0
    rev = 0
    while temp > 0:
        rem = temp % 10
        rev = rev * 10 + rem
        temp = temp // 10
    
    if rev == x:
        return True
    else:
        return False

# Test Case:
print(isPalindrome(1))