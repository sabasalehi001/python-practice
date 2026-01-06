# ChromaShifter

A simple command-line tool for converting between RGB and Hex color codes.

## Usage

Run `python main.py` and follow the prompts to choose a conversion direction and input the color code.

## Example

```
Choose conversion direction:
1. RGB to Hex
2. Hex to RGB
> 1
Enter RGB values (comma-separated, e.g., 255,0,102): 255,0,102
Hex code: #FF0066
```

```
Choose conversion direction:
1. RGB to Hex
2. Hex to RGB
> 2
Enter Hex code (e.g., #FF0000): #FF0000
RGB values: (255, 0, 0)
```

## Error Handling

The program handles invalid input such as incorrect RGB values or malformed Hex codes.
