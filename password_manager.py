import os
import time
from pynput import keyboard

cursor_location = 0
options = ["Create new password", "Show existing passwords", "Exit password manager"]


def display_menu():
    global cursor_location
    global options
    while True:
        print("Use up and down arrow keys to choose action.")
        print("")
        for option in options:
            if option == options[cursor_location]:
                print(f"> {option}")
            else:
                print(f"  {option}")
        time.sleep(1/60)
        os.system('cls' if os.name == 'nt' else 'clear')





def cursor_down():
    global cursor_location
    global options
    if cursor_location == len(options)-1:
        return
    else:
        cursor_location += 1



def cursor_up():
    global cursor_location
    global options
    if cursor_location == 0:
        return
    else:
        cursor_location -= 1





def on_press(key):
    try:
        choice = key.char
    except:
        choice = key.name

    if choice == "down":
        cursor_down()
    elif choice == "up":
        cursor_up()


print("this goes on git")
listener = keyboard.Listener(on_press=on_press)
listener.start()
display_menu()
