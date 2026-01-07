import time

start_time = None
elapsed_time = 0.0

def start_timer():
    global start_time
    global elapsed_time
    if start_time is None:
        start_time = time.time() + elapsed_time
        print("Timer started.")
    else:
        print("Timer is already running.")

def stop_timer():
    global start_time
    global elapsed_time
    if start_time is not None:
        elapsed_time = time.time() - start_time
        start_time = None
        print(f"Timer stopped. Elapsed time: {elapsed_time:.2f} seconds")
    else:
        print("Timer is not running.")

def display_time():
    global start_time
    global elapsed_time
    if start_time is not None:
        current_elapsed_time = time.time() - start_time
        print(f"Current elapsed time: {current_elapsed_time:.2f} seconds")
    else:
        print(f"Total elapsed time: {elapsed_time:.2f} seconds")

def clear_time():
    global start_time
    global elapsed_time
    start_time = None
    elapsed_time = 0.0
    print("Timer reset.")


while True:
    print("\nChronoSculptor")
    print("1. Start Timer")
    print("2. Stop Timer")
    print("3. Display Time")
    print("4. Clear Time")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        start_timer()
    elif choice == '2':
        stop_timer()
    elif choice == '3':
        display_time()
    elif choice == '4':
        clear_time()
    elif choice == '5':
        print("Exiting ChronoSculptor.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
