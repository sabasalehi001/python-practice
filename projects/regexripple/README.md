# RegexRipple

A simple command-line tool for testing regular expressions against input strings.

## Usage

Run `python main.py` and follow the prompts to enter a regular expression and a test string. The program will then display whether the regex matches the string or not, and if so, any captured groups.

## Example

```
$ python main.py

Enter a regular expression: (hello) world
Enter a test string: hello world

Match found!
Captured groups: ['hello']
```

```
$ python main.py

Enter a regular expression: (goodbye) world
Enter a test string: hello world

No match found.
```
