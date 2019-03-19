import os
from pathlib import Path

from midi_file import MidiFile
from midi_constants import MIDI_HEADER_SIG


def is_midi(path):
    with open(path, 'rb') as f:
        return f.read(4) == MIDI_HEADER_SIG


def get_midi_file(path):
    if os.path.isfile(path) and is_midi(path):
        print("Adding midi file - {}".format(Path(path).stem))
        return MidiFile(path)
    else:
        print("No midi file found at location {}".format(path))


def get_midis_from_dir(dir_path):
    midis_found = []
    if os.path.isdir(dir_path):
        for f in os.listdir(dir_path):
            abs_path = os.path.join(dir_path, f)
            if os.path.isfile(abs_path) and is_midi(abs_path):
                midis_found.append(MidiFile(abs_path))
                print("Adding midi file: {}".format(Path(abs_path).stem))
    return midis_found
