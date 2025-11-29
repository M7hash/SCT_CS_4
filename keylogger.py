import datetime

def log_input():
    filename = "logs.txt"

    print("Keylogger Started (type 'exit' to stop):")

    while True:
        user_input = input("> ")

        if user_input.lower() == "exit":
            print("Logging stopped.")
            break

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "a") as f:
            f.write(f"[{timestamp}] {user_input}\n")

        print("Logged.")

log_input()
