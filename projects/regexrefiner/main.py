import re

def validate_regex(regex):
  """Validates if the provided regex is compilable."""
  try:
    re.compile(regex)
    return True
  except re.error:
    return False

def test_regex(regex, test_string):
  """Tests a regular expression against a string and returns True if it matches, False otherwise."""
  match = re.search(regex, test_string)
  return bool(match)

if __name__ == "__main__":
  while True:
    regex = input("Enter your regular expression (or type 'exit' to quit): ")
    if regex.lower() == 'exit':
      break

    if not validate_regex(regex):
      print("Invalid regular expression. Please try again.")
      continue

    test_string = input("Enter your test string: ")

    if test_regex(regex, test_string):
      print("Match found!")
    else:
      print("No match found.")

    print()
