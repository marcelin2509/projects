def romanToInt(s: str) -> int:
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_numerals[char]
        
        if prev_value < value:
            total += value
        else:
            total -= value
        
        prev_value = value
    
    return total


roman = (input("Enter a Roman numeral: "))
integer = romanToInt(roman)
print(f"The integer value of {roman} is: {integer}")