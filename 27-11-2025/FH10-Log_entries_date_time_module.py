from datetime import datetime


def write_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # opening file in append and writing the data entries
    with open("application.log", "a") as log_file:
        log_file.write(f"{timestamp} - {message}\n")

# Example usage
write_log("Application started")
write_log("User logged in")
write_log("Application closed")
