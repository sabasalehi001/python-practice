def to_roman(num):
    if not 1 <= num <= 3999:
        return "Invalid input. Please enter a number between 1 and 3999."

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

def to_integer(roman_num):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0

    for i in range(len(roman_num) - 1, -1, -1):
        curr_value = roman_map.get(roman_num[i])
        if curr_value is None:
            return "Invalid Roman numeral."

        if curr_value < prev_value:
            result -= curr_value
        else:
            result += curr_value
        prev_value = curr_value

    return result

if __name__ == "__main__":
    print("Choose conversion direction:")
    print("1. Integer to Roman")
    print("2. Roman to Integer")

    choice = input("> ")

    if choice == '1':
        try:
            num = int(input("Enter an integer (1-3999):\n> "))
            print(to_roman(num))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    elif choice == '2':
        roman_num = input("Enter a Roman numeral:\n> ").upper()
        print(to_integer(roman_num))
    else:
        print("Invalid choice.")
