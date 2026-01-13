import time

def get_valid_duration():
    while True:
        try:
            duration = float(input("Enter the desired interval duration in seconds (e.g., 1.5): "))
            if duration > 0:
                return duration
            else:
                print("Please enter a positive duration.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def run_practice_session(duration):
    print(f"Starting practice session with {duration} second intervals. Press Enter to mark each interval. Press Ctrl+C to quit.")
    start_time = time.time()
    previous_time = start_time
    try:
        while True:
            input("Press Enter: ")
            current_time = time.time()
            elapsed_time = current_time - previous_time
            difference = elapsed_time - duration
            print(f"Elapsed: {elapsed_time:.2f}s, Difference: {difference:.2f}s")
            previous_time = current_time

    except KeyboardInterrupt:
        print("\nPractice session ended.")

if __name__ == "__main__":
    print("Welcome to TempoTutor!")
    interval_duration = get_valid_duration()
    run_practice_session(interval_duration)
