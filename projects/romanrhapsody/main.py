def to_roman(num):
    roman_map = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
        50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }
    i = 12
    roman_numeral = ''

    while num != 0:
        if list(roman_map.keys())[i] <= num:
            roman_numeral += list(roman_map.values())[i]
            num -= list(roman_map.keys())[i]
        else:
            i -= 1

    return roman_numeral

def from_roman(roman_num):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    i = 0
    while i < len(roman_num):
        if i + 1 < len(roman_num) and roman_map[roman_num[i]] < roman_map[roman_num[i + 1]]:
            result += roman_map[roman_num[i + 1]] - roman_map[roman_num[i]]
            i += 2
        else:
            result += roman_map[roman_num[i]]
            i += 1
    return result


if __name__ == "__main__":
    while True:
        print("Choose conversion direction:")
        print("1. Integer to Roman")
        print("2. Roman to Integer")
        choice = input("> ")

        if choice == '1':
            try:
                num = int(input("Enter an integer (1-3999): "))
                if 1 <= num <= 3999:
                    print("The Roman numeral is:", to_roman(num))
                else:
                    print("Invalid input. Please enter an integer between 1 and 3999.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        elif choice == '2':
            roman_num = input("Enter a Roman numeral: ").upper()
            # very basic validation, just chars
            valid_chars = set(['I', 'V', 'X', 'L', 'C', 'D', 'M'])
            if all(char in valid_chars for char in roman_num):
                print("The integer value is:", from_roman(roman_num))
            else:
                print("Invalid Roman numeral.")

        else:
            print("Invalid choice. Please enter 1 or 2.")
