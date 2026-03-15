import re

def validate_regex(regex_string):
  """Validates that the regex string is not empty.

  Args:
    regex_string: The regex string to validate.

  Returns:
    True if the regex string is valid, False otherwise.
  """
  if not regex_string:
    print("Error: Regular expression cannot be empty.")
    return False
  return True

def test_regex(regex_string, test_string):
  """Tests a regular expression against a test string.

  Args:
    regex_string: The regular expression to test.
    test_string: The string to test against the regular expression.

  Returns:
    A tuple containing:
      - A boolean indicating whether the regex matches the string.
      - A list of captured groups, or None if no match is found.
  """
  try:
    match = re.search(regex_string, test_string)
    if match:
      return True, match.groups()
    else:
      return False, None
  except re.error as e:
    print(f"Error: Invalid regular expression: {e}")
    return False, None

if __name__ == "__main__":
  while True:
    regex_string = input("\nEnter a regular expression (or type 'exit' to quit): ")
    if regex_string.lower() == 'exit':
      break

    if not validate_regex(regex_string):
        continue

    test_string = input("Enter a test string: ")

    match_found, captured_groups = test_regex(regex_string, test_string)

    if match_found:
      print("Match found!")
      if captured_groups:
        print("Captured groups:", captured_groups)
    else:
      print("No match found.")
