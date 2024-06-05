'''
The Roman numeral system consists of the following symbols:
Symbol    Value
I    1
V    5
X    10
L    50
C    100
D    500
M    1000

Numbers are constructed by combining these symbols. For instance, the number 12 can be represented by XII, since X + I + I = 10 + 1 + 1.

The following list is set of rules for Roman numerals:

Zero is not represented.
A symbol can be repeated only for three times.
Roman numerals are repeated to add value: III is equivalent to 1 +1 +1 =  3. However, only powers of 10 may be repeated in this way. Thus, VV is invalid; 5 + 5 would instead be expressed as X.
When a Roman numeral is placed after another Roman numeral of greater value, the result is the sum of the numerals. When a Roman numeral is placed before another Roman numeral of greater value, the result is the difference between the numerals.
Only I, X, and C can be used as subtractive numerals as shown:
I can be used before V(5) and X(10) to make it IV(4) and XV(9) respectively.
X cab be used before L(50) and C(100) to make it XL(40) and XC(90) respectively.
C can be used before D(500) and M(1000) to make them CD(400) and CM(900) respectively.
'''

def roman_converter(number):
    if number == 0:
        return "Zero is not represented in Roman numerals."
    if number >= 4000:
        return "There is no convertion of numbers beyond 3999."

    roman_representation = ''

    # Handling thousands
    if number >= 1000:
        thousands = number // 1000
        roman_representation += 'M' * min(thousands, 3)
        number %= 1000

    # Handling hundreds
    if number >= 100:
        hundreds = number // 100
        if hundreds == 9:
            roman_representation += 'CM'
        elif hundreds >= 5:
            roman_representation += 'D' + 'C' * (hundreds - 5)
        elif hundreds == 4:
            roman_representation += 'CD'
        else:
            roman_representation += 'C' * min(hundreds, 3)
        number %= 100

    # Handling tens
    if number >= 10:
        tens = number // 10
        if tens == 9:
            roman_representation += 'XC'
        elif tens >= 5:
            roman_representation += 'L' + 'X' * (tens - 5)
        elif tens == 4:
            roman_representation += 'XL'
        else:
            roman_representation += 'X' * min(tens, 3)
        number %= 10

    # Handling ones
    if number >= 1:
        ones = number
        if ones == 9:
            roman_representation += 'IX'
        elif ones >= 5:
            roman_representation += 'V' + 'I' * (ones - 5)
        elif ones == 4:
            roman_representation += 'IV'
        else:
            roman_representation += 'I' * min(ones, 3)

    return roman_representation

number = int(input('What number do you want to read in Roman numeral system? '))
print(roman_converter(number))
