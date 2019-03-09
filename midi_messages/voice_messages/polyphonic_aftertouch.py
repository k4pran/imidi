import midi_constants
from midi_messages.midi_message import MidiMessage


class PolyphonicAftertouch(MidiMessage):

    def __init__(self, bdelta, blength, bstatus, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        self.key: int = None
        self.pressure: int = None

    def parse(self):
        self.key = int.from_bytes(self.bdata[0], byteorder='big')
        self.pressure = int.from_bytes(self.bdata[1], byteorder='big')
