#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    roman_values = {
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

    for i in range(len(roman_string) - 1, -1, -1):
        if roman_string[i] not in roman_values:
            return 0

        current_value = roman_values[roman_string[i]]

        if current_value >= prev_value:
            total += current_value
        else:
            total -= current_value

        prev_value = current_value

    return total
