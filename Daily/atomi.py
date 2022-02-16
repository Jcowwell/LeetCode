"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
"""

def atoi(s: str) -> int:
        digit_parsing: bool = False # boolean value to set when digit parsing starts
        sign: int = 1 # sign of number 1 == positive; -1 == negative

        index: int = 0 # index for iterating through parameter s
        length: int = len(s)
        number_str: str = '' # string variable to concatinate valid characters, convert to int, and bound check 

        while index < length:
            if not digit_parsing: # while we are not in digit parsing mode
                if s[index] == ' ':
                    pass # ignore whitespaces
                elif s[index] == '-':
                    sign *= -1
                    digit_parsing = True
                elif s[index] == '+': # sign is positive by default
                    digit_parsing = True
                elif s[index].isdigit():
                    number_str += s[index]
                    digit_parsing = True
                else: # not a valid character
                    break
            else: # while we are in digit parsing mode
                if s[index].isdigit():
                    number_str += s[index]
                else:
                    break
            index += 1

        number: int = int(number_str) * sign if number_str.isdigit() else 0 

        # clamping values within [-2^31, 2^31 - 1] range
        return max(-2**31, 0+number) if number < 0 else min((2**31)-1, number)

atoi(s='   -42')