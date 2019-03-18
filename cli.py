from enum import Enum

from utils_common import *


class Session:

    def __init__(self):
        self.midi_files = []


class Menu(Enum):
    MAIN_MENU = 0


def display(menu):
    if menu == Menu.MAIN_MENU:
        display_main_menu()


def display_main_menu():
    print("--Main Menu--\n")
    print("\t1) Add midi file")
    print("\t2) Add midi folder")
    print("\n\tPress 'q' to exit")


def handle_main(selection):
    if selection == '1':
        path = input("Please enter a path to the midi file")
        midi = get_midi_file(path)
        if midi:
            session.midi_files.append(midi)

    elif selection == '2':
        path = input("Please enter a path to the directory")
        midis = get_midis_from_dir(path)
        [session.midi_files.append(midi) for midi in midis if midi]



def handle_selection(menu, selection):
    if menu == Menu.MAIN_MENU:
        handle_main(selection)


if __name__ == "__main__":
    print("=================")
    print("      IMIDI      ")
    print("=================\n\n")

    session = Session()

    current_menu = Menu.MAIN_MENU
    done = False
    while not done:
        display(current_menu)
        selection = input("\nSelect an option\n\n> ")
        if selection == 'q':
            done = True

        elif current_menu == Menu.MAIN_MENU:
            handle_main(selection)
