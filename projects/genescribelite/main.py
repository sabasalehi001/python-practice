import argparse

def reverse_complement(sequence):
    """Calculates the reverse complement of a DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    reverse = sequence[::-1]
    complement_sequence = ''.join([complement[base] for base in reverse])
    return complement_sequence

def gc_content(sequence):
    """Calculates the GC content of a DNA sequence."""
    gc_count = sequence.upper().count('G') + sequence.upper().count('C')
    return (gc_count / len(sequence)) * 100

def validate_sequence(sequence):
    """Validates if the sequence contains only A, T, G, and C."""
    valid_chars = set('ATGCatgc')
    if not set(sequence).issubset(valid_chars):
        return False
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A simple DNA sequence manipulation tool.')
    parser.add_argument('action', choices=['reverse_complement', 'gc_content'], help='The action to perform.')
    parser.add_argument('sequence', help='The DNA sequence to process.')

    args = parser.parse_args()

    sequence = args.sequence.upper()

    if not validate_sequence(sequence):
        print("Error: Invalid sequence. Only A, T, G, and C are allowed.")
    else:
        if args.action == 'reverse_complement':
            result = reverse_complement(sequence)
            print(f"Reverse Complement: {result}")
        elif args.action == 'gc_content':
            result = gc_content(sequence)
            print(f"GC Content: {result:.2f}% ")
