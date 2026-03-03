# SignalSage: Morse Code Decoder

SignalSage is a simple command-line tool to decode Morse code into readable text. It takes Morse code as input and translates it into English.

## Usage

Run the script using `python main.py`. The program will prompt you to enter the Morse code, using '.' for dots and '-' for dashes. Separate letters with a space and words with '/'.

For example:

```
python main.py
```

Input Morse code: .... . .-.. .-.. --- / .-- --- .-. .-.. -..

Output: HELLO WORLD
```

## Limitations

- Only supports decoding Morse code to English.
- Does not handle invalid Morse code sequences gracefully.
