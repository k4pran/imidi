import midi_constants
from midi_messages.midi_message import MidiMessage


class PitchBend(MidiMessage):

    def __init__(self, bdelta, blength, bstatus, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        self.lsb: int = None
        self.msb: int = None

    def parse(self):
        self.lsb = int.from_bytes(self.bdata[0], byteorder='big')
        self.msb = int.from_bytes(self.bdata[1], byteorder='big')
