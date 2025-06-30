

# Neetcode Solution
# Time Complexity: O(n)
# Space Complexity: O(1)

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    symCode = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    num = 0
    
    for i in range(len(s)):
            if i + 1 < len(s) and symCode[s[i]] < symCode[s[i+1]]:
                num -= symCode[s[i]]
            else:
                num += symCode[s[i]]

    return num

# Test Cases

print(romanToInt("MMM"))
print(romanToInt("MMCMIX"))