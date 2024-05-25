'''
Creating an alarm clock that will ring at a specific time.
Hint 1: use the time module to get the current time and sleep until the alarm time.
Hint 2: start with asking a user what should be executed, like:
Enter '1' to set an alarm
Enter '2' to snooze the alarm
Enter '3' to stop the alarm
Enter '4' to exit 
'''
import time
import winsound

# Version 1:

""" def alarm_clock():
    alarm_time = input("Enter the time you want to get alarmed (format: HH:MM): ")
    current_time = time.strftime("%H:%M")
    print(f"Current time is {current_time} and alarm set for {alarm_time}.")
    while current_time != alarm_time:
        current_time = time.strftime("%H:%M")
        time.sleep(1)
    print("Time to wake up!")
    winsound.Beep(2500, 1000)

alarm_clock() """

#Version 2
def get_time_input():
    while True:
        user_time = input("Enter the alarm time in HH:MM format: ")
        try:
            hours, minutes = map(int, user_time.split(':'))
            if 0 <= hours < 24 and 0 <= minutes < 60:
                return hours, minutes
            else:
                print("Invalid time. Hours must be between 0-23 and minutes between 0-59.")
        except ValueError:
            print("Invalid format. Please use HH:MM format.")

def calculate_seconds_until_alarm(alarm_hour, alarm_minute):
    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min
    current_second = current_time.tm_sec

    current_total_seconds = current_hour * 3600 + current_minute * 60 + current_second
    alarm_total_seconds = alarm_hour * 3600 + alarm_minute * 60

    if alarm_total_seconds >= current_total_seconds:
        return alarm_total_seconds - current_total_seconds
    else:
        return 86400 - (current_total_seconds - alarm_total_seconds)

def play_alarm_sound():
    frequency = 2500
    duration = 1000
    while True:
        winsound.Beep(frequency, duration)
        time.sleep(0.5)
        choice = input("Enter '2' to snooze the alarm, '3' to stop the alarm: ")
        if choice == '2':
            return 'snooze'
        elif choice == '3':
            return 'stop'

def main():
    alarm_set = False
    snooze_duration = 1  # snooze duration in minutes

    while True:
        print("\nEnter '1' to set an alarm")
        print("Enter '4' to exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            alarm_hour, alarm_minute = get_time_input()
            seconds_until_alarm = calculate_seconds_until_alarm(alarm_hour, alarm_minute)
            alarm_set = True
            print(f"Alarm set for {alarm_hour:02d}:{alarm_minute:02d}")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice or no alarm set. Please try again.")

        if alarm_set:
            for remaining_seconds in range(seconds_until_alarm, 0, -1):
                print(f"Time left until alarm: {remaining_seconds} seconds", end='\r')
                time.sleep(1)
            print("\nAlarm ringing! Time to wake up!")
            action = play_alarm_sound()
            if action == 'snooze':
                print(f"Snoozing the alarm for {snooze_duration} minutes...")
                for remaining_seconds in range(snooze_duration * 60, 0, -1):
                    print(f"Snooze time left: {remaining_seconds} seconds", end='\r')
                    time.sleep(1)
                print("\nSnooze time over!")
                alarm_set = True
            elif action == 'stop':
                print("Stopping the alarm...")
                alarm_set = False

#if __name__ == "__main__":
main()
