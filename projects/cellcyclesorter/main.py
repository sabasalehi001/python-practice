def calculate_cycle_score(g1, s, g2m):
 """Calculates a simple 'cycle score' based on the cell cycle percentages.
 This score is a heuristic, and not scientifically rigorous.
 """
 total = g1 + s + g2m
 if total != 100:
 return None  # Indicates invalid input
 score = abs(g1 - s) / 100.0 # Example score, could be any function
 return score

def categorize_cycle_state(score):
 """Categorizes the cell cycle state based on the calculated score.
 """
 if score is None:
 return "Invalid input data."
 if score < 0.15:
 return "Balanced"
 elif score < 0.3:
 return "G1-dominant"
 else:
 return "Unbalanced"

if __name__ == "__main__":
 print("Cell Cycle Sorter")

 while True:
 try:
 g1 = float(input("Enter the percentage of cells in G1 phase: "))
 s = float(input("Enter the percentage of cells in S phase: "))
 g2m = float(input("Enter the percentage of cells in G2/M phase: "))
 if g1 < 0 or s < 0 or g2m < 0:
 print("Percentages must be non-negative.")
 else:
 break
 except ValueError:
 print("Invalid input. Please enter numbers only.")

 score = calculate_cycle_score(g1, s, g2m)

 if score is None:
 print("Error: Percentages must sum to 100.")
 else:
 state = categorize_cycle_state(score)
 print(f"\nCell Cycle Score: {score:.2f}")
 print(f"Cell Cycle State: {state}")
