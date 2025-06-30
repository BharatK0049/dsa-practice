# Seven different symbols represent Roman numerals with the following values:

# Symbol	Value
# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000
# Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

# If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
# If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
# Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
# Given an integer, convert it to a Roman numeral.

# My Solution:
# Time Complexity: O(1)
# Space Complexity: O(1)

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    coding = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}

    num_str = str(num)
    num_list = [int(digit) for digit in num_str]
    for i in range(4-len(num_list)):
        num_list.insert(0, '0')
    
    roman_numeral = ''
    # Base case
    if num in coding:
        roman_numeral = coding[num]
        return roman_numeral
    
    else:
        if num_list[0] > 0 and num_list[0] < 4:
            for i in range(num_list[0]):
                roman_numeral += 'M'
        
        if num_list[1] > 0 and num_list[1] < 10:
            if num_list[1] < 4:
                for i in range(num_list[1]):
                    roman_numeral += 'C'
            elif num_list[1] == 4:
                roman_numeral += 'CD'
            elif num_list[1] == 5:
                roman_numeral += 'D'
            elif num_list[1] > 5 and num_list[1] < 9:
                roman_numeral += 'D'
                for i in range(num_list[1] - 5):
                    roman_numeral += 'C'
            else:
                roman_numeral += 'CM'
        
        if num_list[2] > 0 and num_list[2] < 10:
            if num_list[2] < 4:
                for i in range(num_list[2]):
                    roman_numeral += 'X'
            elif num_list[2] == 4:
                roman_numeral += 'XL'
            elif num_list[2] == 5:
                roman_numeral += 'L'
            elif num_list[2] > 5 and num_list[2] < 9:
                roman_numeral += 'L'
                for i in range(num_list[2] - 5):
                    roman_numeral += 'X'
            else:
                roman_numeral += 'XC'

        if num_list[3] > 0 and num_list[3] < 10:
            if num_list[3] < 4:
                for i in range(num_list[3]):
                    roman_numeral += 'I'
            elif num_list[3] == 4:
                roman_numeral += 'IV'
            elif num_list[3] == 5:
                roman_numeral += 'V'
            elif num_list[3] > 5 and num_list[3] < 9:
                roman_numeral += 'V'
                for i in range(num_list[3] - 5):
                    roman_numeral += 'I'
            else:
                roman_numeral += 'IX'

        return roman_numeral
    


# Test Cases

print(intToRoman(3576))

# Neetcode Solution


def intToRomanShort(num):
    symCode = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL": 40, "X":10, "IX":9, "V":5, "IV":4, "I":1}

    numeral = ''

    for symbol in symCode:
        if num // symCode[symbol]:
            count = num // symCode[symbol]
            numeral += (symbol * count)
            num = num % symCode[symbol]
    
    return numeral

print(intToRomanShort(3576))