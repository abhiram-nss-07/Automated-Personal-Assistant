import os
from tasks.file_organizer import organize_files
from tasks.reminder import create_reminder, check_reminders
from tasks.task_manager import add_task, remove_task, list_tasks
from tasks.weather_fetcher import fetch_weather
from tasks.notification_sender import send_notification

def main():
    print(f"Welcome to your personal assistant, {config.USER_NAME}!")
    while True:
        print("\nWhat would you like to do?")
        print("1. Organize Files")
        print("2. Create Reminder")
        print("3. Check Reminders")
        print("4. Manage Tasks")
        print("5. Fetch Weather Information")
        print("6. Send Notification")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            organize_files()
        elif choice == '2':
            create_reminder()
        elif choice == '3':
            check_reminders()
        elif choice == '4':
            manage_tasks()
        elif choice == '5':
            fetch_weather()
        elif choice == '6':
            send_notification("Here's your custom notification!")
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def manage_tasks():
    print("\nTask Management:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        list_tasks()
    else:
        print("Invalid choice. Returning to main menu.")

if __name__ == "__main__":
    main()
