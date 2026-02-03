import time
import sys

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def run_interval_timer(num_intervals, work_duration, rest_duration):
    print("\nStarting timer...\n")
    for i in range(num_intervals):
        print(f"Work interval {i+1}/{num_intervals}: {work_duration} seconds remaining")
        time.sleep(work_duration)
        print(f"Rest interval {i+1}/{num_intervals}: {rest_duration} seconds remaining")
        time.sleep(rest_duration)
    print("\nTimer complete!")


if __name__ == "__main__":
    num_intervals = get_positive_int("Number of intervals: ")
    work_duration = get_positive_int("Work duration (seconds): ")
    rest_duration = get_positive_int("Rest duration (seconds): ")
    
    run_interval_timer(num_intervals, work_duration, rest_duration)
