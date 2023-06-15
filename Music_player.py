# This will need to be swaped out for a locally accessible audio module
from replit import audio
import os
import time


def play():
    source = audio.play_file('audio.wav')
    source.paused = False  # unpause the playback
    while True:
        # Start taking user input and doing something with it
        user_input = input(
            "Press 'p' to PAUSE\nPress 'u' to UNPAUSE\nPress 'e' to EXIT\n")
        os.system("clear")
        if user_input.lower() == 'p':
            source.paused = True  # pause the playback
            print("Playback paused.")
        elif user_input.lower() == 'u':
            source.paused = False  # unpause the playback
            print("Playback resumed.")
        elif user_input.lower() == 'e':
            source.paused = True  # unpause the playback
            print("Playback stopped. Back to Main Menu.")
            time.sleep(2)
            break


while True:
    # clear the screen
    os.system("clear")  # use os.system("cls") if you are on windows

    # Show the menu
    print("Welcome to the music player!")
    print("Press 'p' to PLAY\nPress 'e' to EXIT")
    # take user's input
    user_input = input()
    os.system("clear")

    # check whether you should call the play() subroutine depending on user's input
    if user_input.lower() == 'p':
        play()
    elif user_input.lower() == 'e':
        print("Exiting...")
        time.sleep(1)
        os.system("clear")
        break
    else:
        print("Invalid input. Please try again.")
        # sleep for 1 second to allow user to read the message before the screen is cleared
        time.sleep(1)
