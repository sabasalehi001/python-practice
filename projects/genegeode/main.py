import sys

def validate_sequence(sequence):
    """Validates if the input sequence contains only valid DNA bases."""
    valid_bases = "ATGCatgc"
    for base in sequence:
        if base not in valid_bases:
            return False
    return True

def calculate_gc_content(sequence):
    """Calculates the GC content of a DNA sequence."""
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    total_count = len(sequence)
    if total_count == 0:
        return 0.0
    return (gc_count / total_count) * 100

def reverse_complement(sequence):
    """Calculates the reverse complement of a DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    reverse_seq = sequence[::-1]
    complement_seq = ''.join([complement[base] for base in reverse_seq])
    return complement_seq


if __name__ == "__main__":
    while True:
        print("\nChoose an operation:")
        print("1. Calculate GC content")
        print("2. Reverse complement")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            sequence = input("Enter a DNA sequence: ")
            if not validate_sequence(sequence):
                print("Invalid sequence. Please enter a sequence containing only A, T, G, and C.")
                continue
            gc_content = calculate_gc_content(sequence)
            print(f"GC content: {gc_content:.2f}%\n")

        elif choice == '2':
            sequence = input("Enter a DNA sequence: ")
            if not validate_sequence(sequence):
                print("Invalid sequence. Please enter a sequence containing only A, T, G, and C.")
                continue
            reverse_complement_seq = reverse_complement(sequence)
            print(f"Reverse complement: {reverse_complement_seq}\n")

        elif choice == '3':
            print("Exiting...")
            sys.exit()

        else:
            print("Invalid choice. Please enter a number between 1 and 3.\n")
