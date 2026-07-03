import time
import os
import pyttsx3
from plyer import notification
import threading

engine = pyttsx3.init()
voice = True
reminder_running = False

def set_time():

    print("Set Reminder Timelaps(min)")

    try:
        user_set_time = int(input("Choose :"))

        if user_set_time <= 0:
            print("Enter Real Numbers Only")
            return
        
    except ValueError:
        print("Invalid Input")
        return

    threading.Thread(
    target=set_reminder,
    args=(user_set_time,),
    daemon=True
    ).start()

    global reminder_running
    reminder_running = True



def set_reminder(user_set_time):

    while True:

        time.sleep(user_set_time *60)
        print("Sending.....")
        notification.notify (
            title = "Water Reminder",
            message ="Pani Pee Looo",
            timeout = 10
        )
        
        if voice:
            engine.say("Pani Pee Loo")
            engine.runAndWait()


def voice_off():

    global voice 
    voice = False
    print("Turning Voice-Notification Off")

MENU = [
    ("Set Water Reminder",  set_time),
    ("Turn Off Voice Remindder",  voice_off),
    ("Exit",  None)
]


#Just Some Cool Stufff
def main():

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" + "=" * 55)
        print("  Water Reminder Tool")
        print("=" * 55)
        for i, (label, _) in enumerate(MENU, 1):
            print(f"   {i}.  {label}")
        print("=" * 55)

        try:
            choice = int(input("\n  Enter option: ").strip())
        except (ValueError, KeyboardInterrupt):
            print("\n  Invalid input. Try again.")
            input("\n  Press Enter to continue...")
            continue

        if choice < 1 or choice > len(MENU):
            print("  Out of range.")
            input("\n  Press Enter to continue...")
            continue

        if choice == 1 and reminder_running == True:
            print(f"You Already Set Reminder For Every Minutes")
            input("\n  Press Enter to continue...")
            continue


        label, action = MENU[choice - 1]
        if action is None:
            print("\n  Goodbye!\n")
            break

        action()

        input("\n  Press Enter to return to menu...")

if __name__ == "__main__":
    main()
