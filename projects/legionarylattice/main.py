def to_roman(num):
    roman_map = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
                  100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    i = 12
    roman_numeral = ''
    while num != 0:
        if list(roman_map.keys())[i] <= num:
            roman_numeral += list(roman_map.values())[i]
            num -= list(roman_map.keys())[i]
        else:
            i -= 1
    return roman_numeral

def to_integer(roman):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    i = 0
    while i < len(roman):
        if i + 1 < len(roman) and roman_map[roman[i]] < roman_map[roman[i+1]]:
            result += roman_map[roman[i+1]] - roman_map[roman[i]]
            i += 2
        else:
            result += roman_map[roman[i]]
            i += 1
    return result

if __name__ == "__main__":
    print("Welcome to LegionaryLattice!")
    while True:
        conversion_type = input("Convert to Roman or Integer? (r/i): ").lower()
        if conversion_type not in ('r', 'i'):
            print("Invalid input. Please enter 'r' or 'i'.")
            continue

        if conversion_type == 'r':
            try:
                num = int(input("Enter integer (1-3999): "))
                if 1 <= num <= 3999:
                    print("Roman numeral:", to_roman(num))
                    break
                else:
                    print("Invalid input. Please enter an integer between 1 and 3999.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        else:
            roman_numeral = input("Enter Roman numeral: ").upper()
            try:
                integer_value = to_integer(roman_numeral)
                # Check for invalid Roman numerals by converting back and comparing
                if to_roman(integer_value) == roman_numeral:
                    print("Integer:", integer_value)
                    break
                else:
                     print("Invalid Roman numeral.")
            except KeyError:
                print("Invalid Roman numeral.")
