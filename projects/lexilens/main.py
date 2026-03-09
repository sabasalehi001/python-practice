import re
import sys

def validate_regex(regex):
    try:
        re.compile(regex)
        return True
    except re.error:
        return False

def test_regex(regex, text):
    try:
        match = re.search(regex, text)
        if match:
            print("Match found:")
            print(f"  Start: {match.start()}")
            print(f"  End: {match.end()}")
            print(f"  Group(0): {match.group(0)}")
            if len(match.groups()) > 0:
               for i in range(1, len(match.groups()) + 1):
                   print(f"  Group({i}): {match.group(i)}")
        else:
            print("No match found.")
    except Exception as e:
        print(f"Error during regex execution: {e}")

def main():
    print("LexiLens: A Simple Regex Tester\n")

    if len(sys.argv) > 1:
        if len(sys.argv) != 3:
            print("Usage: python main.py <regex> <text>")
            return
        regex = sys.argv[1]
        text = sys.argv[2]
    else:
        regex = input("Enter regular expression: ")
        text = input("Enter text to test against: ")

    if not validate_regex(regex):
        print("Invalid regular expression.")
        return

    test_regex(regex, text)

if __name__ == "__main__":
    main()
