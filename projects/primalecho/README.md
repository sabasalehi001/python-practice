# PrimalEcho: Prime Number Harmonic Resonance

PrimalEcho is a simple command-line tool that explores prime numbers and their harmonic relationships. It takes a range of numbers as input and identifies prime numbers within that range. Further, it calculates a 'resonance' score for each prime, based on its proximity to the average of the range. This resonance score gives a sense of how 'harmonically central' the prime is within the given numerical interval.

## Usage

```bash
python main.py <start_number> <end_number>
```

**Example:**

```bash
python main.py 1 20
```

This will output the prime numbers between 1 and 20, along with their resonance scores.

## Explanation

*   **Prime Number Identification:** The program uses a basic primality test to identify prime numbers within the given range.
*   **Resonance Score:** The resonance score is calculated as the absolute difference between the prime number and the midpoint of the range. A lower score indicates a prime number closer to the center of the range, suggesting a greater 'harmonic resonance'.

## Note

This is a beginner project intended for educational purposes. It's not optimized for performance on very large ranges.
