from enum import Enum

from utils_common import *


class Session:

    def __init__(self):
        self.midi_files = {}
        self.selected: MidiFile = None

    def select_midi(self, name):
        midi = self.midi_files.get(name)
        if midi:
            self.selected = midi
            print("\nMidi: {} selected\n".format(self.selected.name))
        else:
            print("No midi file with name {}. Try listing available midi files".format(name))

    def print_midi_names(self):
        if len(self.midi_files) == 0:
            print("No midi files available. Try adding some")
            return
        print("")
        for midi in self.midi_files:
            print("\t- " + self.midi_files[midi].name)
        print("")


class Menu(Enum):
    MAIN_MENU = 0


def display(menu):
    if menu == Menu.MAIN_MENU:
        display_main_menu()


def display_main_menu():
    print("--Main Menu--\n")
    print("\t1) Add midi file")
    print("\t2) Add midi folder")
    print("\t3) Select a midi file")
    print("\t4) List midi files")
    print("\n\tPress 'q' to exit")


def handle_main(selection):
    if selection == '1':
        path = input("Please enter a path to the midi file\n> ")
        midi = get_midi_file(path)
        if midi:
            session.midi_files[midi.name.lower()] = midi

    elif selection == '2':
        path = input("Please enter a path to the directory\n> ")
        midis = get_midis_from_dir(path)
        for midi in midis:
            if midi:
                session.midi_files[midi.name.lower()] = midi

    elif selection == '3':
        name = input("Enter name of midi file\n> ")
        session.select_midi(name.lower())

    elif selection == '4':
        session.print_midi_names()


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
