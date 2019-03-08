import midi_constants
from midi_messages.midi_message import MidiMessage


class NoteOff(MidiMessage):

    def __init__(self, bstatus, bdata):
        super().__init__(bstatus, midi_constants.NOTE_OFF_DATA_SIZE, bdata)
        self.key: int = None
        self.velocity: int = None

    def parse(self):
        self.key = int.from_bytes(self.bdata[0], byteorder='big')
        self.velocity = int.from_bytes(self.bdata[1], byteorder='big')
