def BasicRomanNumerals(strParam):
    # Map of Roman numerals to their decimal values
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    result = 0
    i = 0
    
    # Process the string character by character
    while i < len(strParam):
        # Current numeral value
        current = roman_numerals[strParam[i]]
        
        # Next numeral value (if it exists)
        next_val = roman_numerals[strParam[i+1]] if i + 1 < len(strParam) else 0
        
        # If current is less than next, it's a subtraction case
        if current < next_val:
            result += next_val - current
            i += 2  # Skip the next numeral since we've already used it
        else:
            result += current
            i += 1
    
    return result

# Test cases
print(BasicRomanNumerals("XXIV"))  # Should output 24
print(BasicRomanNumerals("IV"))    # Should output 4
print(BasicRomanNumerals("MCMXCIV"))  # Should output 1994
print(BasicRomanNumerals("III"))   # Should output 3
