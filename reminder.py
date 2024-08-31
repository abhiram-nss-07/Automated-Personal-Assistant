import time
import config
from utils.helper import read_lines_from_file, write_lines_to_file

def create_reminder():
    reminder_time = input("Enter reminder time (HH:MM format): ")
    reminder_message = input("Enter reminder message: ")

    with open(config.REMINDER_FILE, "a") as file:
        file.write(f"{reminder_time},{reminder_message}\n")
    print("Reminder set successfully!")

def check_reminders():
    reminders = read_lines_from_file(config.REMINDER_FILE)
    current_time = time.strftime("%H:%M")

    for reminder in reminders:
        reminder_time, reminder_message = reminder.split(",")
        if reminder_time == current_time:
            print(f"Reminder: {reminder_message.strip()}")
            send_notification(reminder_message.strip())
