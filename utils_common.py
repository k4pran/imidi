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
            if os.path.isfile(f) and is_midi(f):
                midis_found.append(MidiFile(f))
                print("Adding midi file: {}".format(Path(f).stem))
    return midis_found
