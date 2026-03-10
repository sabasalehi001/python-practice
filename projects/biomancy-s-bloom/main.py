def dna_to_rna(dna_sequence):
    """Converts a DNA sequence to an RNA sequence."""
    if not isinstance(dna_sequence, str):
        raise TypeError("DNA sequence must be a string.")
    if not all(base in 'ATGC' for base in dna_sequence.upper()):
        raise ValueError("Invalid DNA sequence. Contains characters other than A, T, G, and C.")
    return dna_sequence.upper().replace('T', 'U')


def calculate_gc_content(dna_sequence):
    """Calculates the GC content of a DNA sequence."""
    if not isinstance(dna_sequence, str):
        raise TypeError("DNA sequence must be a string.")
    if not all(base in 'ATGC' for base in dna_sequence.upper()):
        raise ValueError("Invalid DNA sequence. Contains characters other than A, T, G, and C.")
    dna_sequence = dna_sequence.upper()
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    total_count = len(dna_sequence)
    if total_count == 0:
        return 0.0  # Avoid division by zero
    return (gc_count / total_count) * 100


if __name__ == "__main__":
    while True:
        print("\nBiomancy's Bloom")
        print("1. Convert DNA to RNA")
        print("2. Calculate GC Content")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            dna = input("Enter DNA sequence: ")
            try:
                rna = dna_to_rna(dna)
                print("RNA sequence:", rna)
            except (TypeError, ValueError) as e:
                print("Error:", e)
        elif choice == '2':
            dna = input("Enter DNA sequence: ")
            try:
                gc_content = calculate_gc_content(dna)
                print("GC content: {:.2f}%".format(gc_content))
            except (TypeError, ValueError) as e:
                print("Error:", e)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
