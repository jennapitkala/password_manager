import os
import time
from pynput import keyboard

cursor_location = 0
options = ["Create new password", "Show existing passwords", "Exit password manager"]
showing_menu = True

def display_menu():
    global listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    global cursor_location
    global options
    global showing_menu
    while True:
        if showing_menu:
            print("Use up and down arrow keys to choose action.")
            print("")
            for option in options:
                if option == options[cursor_location]:
                    print(f"> {option}")
                else:
                    print(f"  {option}")
            time.sleep(1/60)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            time.sleep(1/60)





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


def create_new_password():
    global cursor_location
    cursor_location = 0
    global options
    options = ["Generate a random password", "Create your own password", "Go back"]


def show_passwords():
    return



def make_choice():
    global showing_menu
    if cursor_location == 0:
        create_new_password()
    elif cursor_location == 1:
        show_passwords()
    elif cursor_location == 2:
        return


def on_press(key):
    try:
        choice = key.char
    except:
        choice = key.name

    if choice == "down":
        cursor_down()
    elif choice == "up":
        cursor_up()
    elif choice == "b":
        make_choice()




display_menu()
input("")
