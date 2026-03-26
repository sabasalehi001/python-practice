import time

def start_stopwatch():
    """Starts and stops a stopwatch, displaying the elapsed time."""
    input("Press Enter to start the stopwatch...")
    start_time = time.time()
    input("Press Enter to stop the stopwatch...")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

def start_countdown_timer(duration):
    """Starts a countdown timer for a specified duration."""
    if not isinstance(duration, (int, float)) or duration <= 0:
        print("Invalid duration. Please enter a positive number.")
        return

    print(f"Starting countdown timer for {duration:.0f} seconds...")
    time.sleep(duration)
    print("Countdown complete!")

if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. Stopwatch")
        print("2. Countdown Timer")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            start_stopwatch()
        elif choice == '2':
            try:
                duration = float(input("Enter the duration in seconds: "))
                start_countdown_timer(duration)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
