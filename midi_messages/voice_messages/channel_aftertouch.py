import midi_constants
from midi_messages.midi_message import MidiMessage


class ChannelAftertouch(MidiMessage):

    def __init__(self, bdelta, blength, bstatus, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        self.pressure: int = None

    def parse(self):
        self.pressure = int.from_bytes(self.bdata, byteorder='big')
